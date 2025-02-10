from fastapi import APIRouter
from app.database import database
from app.models import items
from app.schemas.item import Item

router = APIRouter()

@router.post("/")
async def create_item(item: Item):
    query = items.insert().values(**item.dict())
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "message": "Item created successfully"}
