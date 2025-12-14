import json
from fastapi import FastAPI, Query
from src.config import RETAILCRM_SITE
from src.retailcrm import retailcrm_get, retailcrm_post
from typing import Optional

from src.schemas import (
    CustomerCreate,
    OrderCreate,
    PaymentCreate
)

app = FastAPI()


@app.post("/customers/")
async def create_customer(customer: CustomerCreate):
    customer_data = {
        "firstName": customer.firstName,
        "email": customer.email,
        "phones": (
            [{"number": customer.phone}]
            if customer.phone else []
        ),
    }

    data = {
        "site": RETAILCRM_SITE,
        "customer": json.dumps(customer_data),
    }

    return await retailcrm_post(
        "/api/v5/customers/create",
        data
    )


@app.get("/customers/")
async def get_customers(
    name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    created_at_from: Optional[str] = Query(None),
):
    params = {}

    if name:
        params["filter[name]"] = name
    if email:
        params["filter[email]"] = email
    if created_at_from:
        params["filter[createdAtFrom]"] = created_at_from

    return await retailcrm_get("/api/v5/customers", params)


@app.post("/orders/")
async def create_order(order: OrderCreate):
    order_data = {
        "orderNumber": order.orderNumber,
        "customer": {"id": order.customerId},
        "items": [
            {
                "productName": item.productName,
                "quantity": item.quantity,
                "initialPrice": item.initialPrice,
            }
            for item in order.items
        ],
    }

    payload = {
        "site": RETAILCRM_SITE,
        "order": json.dumps(order_data),
    }

    return await retailcrm_post(
        "/api/v5/orders/create",
        payload
    )


@app.get("/customers/{customer_id}/orders/")
async def get_customer_orders(customer_id: int):
    return await retailcrm_get(
        "/api/v5/orders",
        params={"filter[customerId]": customer_id}
    )


@app.post("/payments/")
async def create_payment(payment: PaymentCreate):
    payment_data = {
        "order": {"id": payment.orderId},
        "amount": payment.amount,
        "type": "cash"
    }

    data = {
        "site": RETAILCRM_SITE,
        "payment": json.dumps(payment_data)
    }

    endpoint = "/api/v5/orders/payments/create"

    return await retailcrm_post(endpoint, data)
