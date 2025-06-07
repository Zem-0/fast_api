from fastapi import FastAPI
from app.database import engine
import app.models as models
from fastapi.middleware.cors import CORSMiddleware
from app.routers.meetings import router as meetings_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "https://todo-ashen-ten-16.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(meetings_router, prefix="/api/meetings", tags=["meetings"])
