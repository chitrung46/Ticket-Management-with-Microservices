"""
This module contains the base interface for CRUD (Create, Read, Update, Delete)
operations using MongoDB with Motor.
"""

from typing import List, Optional, Type, TypeVar, Generic
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from datetime import datetime
from bson import ObjectId
from datetime import datetime

SchemaType = TypeVar("SchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDRepository(Generic[SchemaType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection: AsyncIOMotorCollection, model: Type[SchemaType]):
        self.collection = collection
        self.model = model

    async def get_one(self, id: str) -> Optional[SchemaType]:
        data = await self.collection.find_one({"_id": ObjectId(id)})
        return self.model(**data) if data else None

    async def get_many(self, skip: int = 0, limit: int = 100) -> List[SchemaType]:
        cursor = self.collection.find().skip(skip).limit(limit)
        return [self.model(**doc) async for doc in cursor]

    async def create(self, obj_create: CreateSchemaType) -> SchemaType:
        obj_data = obj_create.model_dump(by_alias=True)
        obj_data["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(obj_data)
        created = await self.collection.find_one({"_id": result.inserted_id})
        return self.model(**created)

    async def update(self, id: str, obj_update: UpdateSchemaType) -> Optional[SchemaType]:
        update_data = obj_update.model_dump(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        updated = await self.collection.find_one({"_id": ObjectId(id)})
        return self.model(**updated) if updated else None

    async def delete(self, id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count == 1
