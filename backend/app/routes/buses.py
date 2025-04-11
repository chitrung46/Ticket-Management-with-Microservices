from fastapi import APIRouter
from models.buses import Bus
from core.db.databases import collection_name
from schemas.buses import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/buses")
async def get_buses():
    buses = list_serial(collection_name.find())
    return buses

@router.post("/buses")
async def post_bus(bus: Bus):
    collection_name.insert_one(dict(bus))

@router.put("/buses/{bus_id}")
async def put_bus(bus_id: str, bus: Bus):
    collection_name.find_one_and_update({"_id": ObjectId(bus_id)}, {"$set": dict(bus)}) 

@router.delete("/buses/{bus_id}")
async def delete_bus(bus_id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(bus_id)})