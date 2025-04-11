from pydantic import BaseModel

class Bus(BaseModel):
    brand: str
    num_plate: str
    color: str
    bus_type_id: str

class BusType(BaseModel):
    name: str