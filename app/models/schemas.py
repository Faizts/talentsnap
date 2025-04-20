# app/schemas/resume.py
from typing import Optional, List
from pydantic import BaseModel
class ResumeMetadata(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    city: Optional[str]
    linkedin_url: Optional[str]
    github_url: Optional[str]

class ResumeScore(BaseModel):
    filename: str
    match_score: float
    metadata: ResumeMetadata

class ResumeScoreResponse(BaseModel):
    results: list[ResumeScore]

class SingleResumeResponse(BaseModel):
    filename: str
    match_score: float
    metadata: ResumeMetadata
