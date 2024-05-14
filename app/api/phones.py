from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import PhoneOut, PhoneIn
from app.api import db_manager

phones = APIRouter()

@phones.post('/', response_model=PhoneOut, status_code=201)
async def create_phone(payload: PhoneIn):
    phone_id = await db_manager.add_phone(payload)

    response = {
        'id': phone_id,
        **payload.dict()
    }

    return response


@phones.get('/', response_model=List[PhoneOut])
async def get_phones():
    return await db_manager.get_all_phone()


@phones.get('/{id}/', response_model=PhoneOut)
async def get_phone(id: int):
    company = await db_manager.get_phone(id)
    if not company:
        raise HTTPException(status_code=404, detail="phone not found")
    return company


@phones.delete('/{id}/', response_model=None)
async def delete_phone(id: int):
    company = await db_manager.get_phone(id)
    if not company:
        raise HTTPException(status_code=404, detail="phone not found")
    return await db_manager.delete_phone(id)