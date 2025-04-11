from fastapi import FastAPI
from routes.buses import router as bus_router

app = FastAPI()

app.include_router(bus_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
