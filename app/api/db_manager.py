from app.api.models import PhoneIn, PhoneOut
from app.api.db import phones, database


async def add_phone(payload: PhoneIn):
    query = phones.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_phone():
    query = phones.select()
    return await database.fetch_all(query=query)


async def get_phone(id):
    query = phones.select().where(phones.c.id == id)
    return await database.fetch_one(query=query)


async def delete_phone(id: int):
    query = phones.delete().where(phones.c.id == id)
    return await database.execute(query=query)

