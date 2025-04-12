from fastapi import FastAPI
from routes import bus

app = FastAPI()

app.include_router(bus.router, prefix="/buses", tags=["Buses"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}
