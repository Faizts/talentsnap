from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  

def match_resume_to_job(resume_text: str, job_description: str) -> float:
    embeddings = model.encode([resume_text, job_description])
    similarity_score = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
    return float(round(similarity_score, 2))  # Convert numpy.float32 to native Python float
