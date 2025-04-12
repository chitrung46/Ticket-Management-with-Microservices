from crud.base import CRUDRepository
from schemas.bus import Bus, BusCreate, BusUpdate
from motor.motor_asyncio import AsyncIOMotorCollection

class BusCRUD(CRUDRepository[Bus, BusCreate, BusUpdate]):
    def __init__(self, collection: AsyncIOMotorCollection):
        super().__init__(collection, Bus)