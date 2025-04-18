from fastapi import APIRouter, UploadFile, File, HTTPException # type: ignore
from app.services.parser import parse_resume
from app.services.matcher import match_resume_to_job
from pydantic import BaseModel # type: ignore

router = APIRouter()

# Route to upload resume PDF
@router.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        content = await file.read()
        resume_text = parse_resume(content)

        job_description = "Example job description text..."
        match_score = match_resume_to_job(resume_text, job_description)

        return {"resume_text": resume_text, "match_score": match_score}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
