# TalentSnap

TalentSnap is a FastAPI-based application designed to streamline the process of matching resumes to job descriptions. It provides an API for uploading resumes in PDF format and comparing them against job descriptions to calculate a match score.

## Features

- **Resume Parsing**: Extracts text from uploaded PDF resumes.
- **Job Matching**: Compares the parsed resume text with a provided job description and calculates a match score.
- **API Endpoints**: Provides RESTful endpoints for interacting with the application.

## Project Structure

```
app/
├── __init__.py
├── main.py
├── models/
│   ├── __init__.py
│   └── schemas.py
├── routes/
│   ├── __init__.py
│   └── resume.py
├── services/
│   ├── __init__.py
│   ├── matcher.py
│   └── parser.py
```

### Key Directories

- **`models/`**: Contains data models and schemas used in the application.
- **`routes/`**: Defines the API routes, including the `upload-resume` endpoint.
- **`services/`**: Implements the core logic for parsing resumes and matching them to job descriptions.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd talentsnap
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Upload Resume

**POST** `/upload-resume/`

- **Description**: Upload a resume in PDF format and provide a job description to calculate a match score.
- **Parameters**:
  - `file`: The resume file in PDF format.
  - `job_description`: A string containing the job description.
- **Response**:
  - `resume_text`: The extracted text from the resume.
  - `match_score`: The calculated match score between the resume and the job description.

## Dependencies

- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **PyPDF2**: Library for parsing PDF files.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For inquiries, please contact the project maintainer.