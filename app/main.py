from fastapi import FastAPI
from app.routes.resume import router as resume_router

app = FastAPI()

# Include the resume routes
app.include_router(resume_router)
