from fastapi import APIRouter, HTTPException, Depends
from typing import List
from schemas.bus import Bus, BusCreate, BusUpdate
from crud.bus import BusCRUD
from core.db.databases import bus_db
from bson import ObjectId

router = APIRouter()
bus_crud = BusCRUD(bus_db["bus"])

def validate_object_id(id: str) -> ObjectId:
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    return ObjectId(id)


@router.post("/", response_model=Bus)
async def create_bus(bus: BusCreate):
    return await bus_crud.create(bus)


@router.get("/", response_model=List[Bus])
async def get_buses(skip: int = 0, limit: int = 10):
    return await bus_crud.get_many(skip=skip, limit=limit)


@router.get("/{bus_id}", response_model=Bus)
async def get_bus(bus_id: str):
    bus = await bus_crud.get_one(bus_id)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return bus


@router.put("/{bus_id}", response_model=Bus)
async def update_bus(bus_id: str, update_data: BusUpdate):
    updated = await bus_crud.update(bus_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Bus not found")
    return updated


@router.delete("/{bus_id}")
async def delete_bus(bus_id: str):
    success = await bus_crud.delete(bus_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {"deleted": True}
