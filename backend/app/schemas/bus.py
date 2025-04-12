from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from schemas.utils import PyObjectId
from datetime import datetime

class BusType(BaseModel):
    name: str

class BusBase(BaseModel):
    brand: str
    num_plate: str
    color: str
    bus_type_id: str

class BusCreate(BusBase):
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat(),
        }

class BusUpdate(BaseModel):
    brand: Optional[str] = None
    num_plate: Optional[str] = None
    color: Optional[str] = None
    bus_type_id: Optional[str] = None
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat(),
        }

class Bus(BusBase):
    # id: PyObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat(),
        }