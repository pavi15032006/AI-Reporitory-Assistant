from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import repository
from app.routers import scanner
from app.routers import qa

app = FastAPI()

# Allow React Frontend to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(repository.router)
app.include_router(scanner.router)
app.include_router(qa.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Repository Assistant API"
    }