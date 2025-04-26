from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import bus

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Chỉ cho phép frontend từ cổng 5500
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả phương thức HTTP (GET, POST, PUT, DELETE, v.v.)
    allow_headers=["*"],  # Cho phép tất cả các header
)

app.include_router(bus.router, prefix="/buses", tags=["Buses"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}
