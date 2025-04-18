from fastapi import APIRouter, UploadFile, File, HTTPException, Form # type: ignore
from app.services.parser import parse_resume
from app.services.matcher import match_resume_to_job
from pydantic import BaseModel # type: ignore

router = APIRouter()

# Route to upload resume PDF
@router.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    # check for empty strings
    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")
    # check for None values
    if job_description is None:
        raise HTTPException(status_code=400, detail="Job description is required.")
    if file is None:
        raise HTTPException(status_code=400, detail="File is required.")
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    try:
        content = await file.read()
        resume_text = parse_resume(content)
        match_score = match_resume_to_job(resume_text, job_description)
        return {"resume_text": resume_text, "match_score": match_score}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
# multipale file upload 
@router.post("/upload-resumes-multiple/")
async def upload_resumes_multiple(files: list[UploadFile] = File(...), job_description: str = Form(...)):
    # check for empty strings
    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")
    # check for None values
    if job_description is None:
        raise HTTPException(status_code=400, detail="Job description is required.")
    if files is None:
        raise HTTPException(status_code=400, detail="Files are required.")
    if not all(file.filename.endswith(".pdf") for file in files):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    try:
        results = []
        for file in files:
            content = await file.read()
            resume_text = parse_resume(content)
            match_score = match_resume_to_job(resume_text, job_description)
            results.append({"resume_text": resume_text, "match_score": match_score})
        return {"results": results}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
