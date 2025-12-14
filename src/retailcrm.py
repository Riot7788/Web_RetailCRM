import httpx
from src.config import RETAILCRM_URL, RETAILCRM_API_KEY
from fastapi import HTTPException


async def retailcrm_get(endpoint: str, params: dict | None = None):
    async with httpx.AsyncClient(base_url=RETAILCRM_URL) as client:
        response = await client.get(
            endpoint,
            params={
                "apiKey": RETAILCRM_API_KEY,
                **(params or {})
            }
        )
        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()


async def retailcrm_post(endpoint: str, data: dict):
    async with httpx.AsyncClient(base_url=RETAILCRM_URL) as client:
        response = await client.post(
            endpoint,
            data=data,
            params={"apiKey": RETAILCRM_API_KEY},
        )

        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()
