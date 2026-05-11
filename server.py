
from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, students,ai
from database import Base, engine
from dotenv import load_dotenv
load_dotenv()
import models.user
import models.student
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authentication API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(students.router,prefix="/students",tags=["students"])
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "Auth API is running"}
    
