# app/routes/resume.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.parser import parse_resume
from app.services.matcher import match_resume_to_job
from app.models.schemas import ResumeScoreResponse, SingleResumeResponse
from app.services.extractor import extract_resume_entities

router = APIRouter()

def validate_job_desc(job_description: str):
    if not job_description or not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

def validate_file(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

@router.post("/upload-resume/", response_model=SingleResumeResponse)
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    validate_job_desc(job_description)
    validate_file(file)

    try:
        content = await file.read()
        resume_text = parse_resume(content)
        match_score = match_resume_to_job(resume_text, job_description)
        metadata = extract_resume_entities(resume_text)
        return {"filename": file.filename, "match_score": match_score, "metadata": metadata}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.post("/upload-resumes-multiple/", response_model=ResumeScoreResponse)
async def upload_resumes_multiple(files: list[UploadFile] = File(...), job_description: str = Form(...)):
    validate_job_desc(job_description)

    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded.")

    for file in files:
        validate_file(file)

    try:
        results = []
        for file in files:
            content = await file.read()
            resume_text = parse_resume(content)
            match_score = match_resume_to_job(resume_text, job_description)
            metadata = extract_resume_entities(resume_text)
            results.append({"filename": file.filename, "match_score": match_score, "metadata": metadata})

        results = [{"filename": r["filename"], "match_score": r["match_score"] * 100, "metadata": r["metadata"]} for r in results]
        results.sort(key=lambda x: x["match_score"], reverse=True)
        return {"results": results}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
