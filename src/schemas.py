from pydantic import BaseModel
from typing import List, Optional


class CustomerCreate(BaseModel):
    firstName: str
    email: Optional[str] = None
    phone: Optional[str] = None


class OrderItem(BaseModel):
    productName: str
    quantity: int
    initialPrice: float


class OrderCreate(BaseModel):
    customerId: int
    orderNumber: str
    items: List[OrderItem]


class PaymentCreate(BaseModel):
    orderId: int
    amount: float