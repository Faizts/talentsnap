import re
from typing import Optional
from urllib.parse import urlparse
from app.services.location_extractor import extract_city_from_text

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"\+?\d[\d\s().-]{7,}\d"
LINKEDIN_REGEX = r"https?://(www\.)?linkedin\.com/in/[a-zA-Z0-9\-_/]+"
GITHUB_REGEX = r"https?://(www\.)?github\.com/[a-zA-Z0-9\-_/]+"


def extract_resume_entities(text: str) -> dict:
    # Normalize text
    lower_text = text.lower()

    # Extract name: first line or first capitalized word (very basic)
    name = text.strip().split('\n')[0] if text else None
    name = name.strip() if name and len(name.split()) < 6 else None

    # Extract email
    email_match = re.search(EMAIL_REGEX, text)
    email = email_match.group(0) if email_match else None

    # Extract phone
    phone_match = re.search(PHONE_REGEX, text)
    phone = phone_match.group(0) if phone_match else None

    # Extract LinkedIn & GitHub
    linkedin_match = re.search(LINKEDIN_REGEX, text, re.IGNORECASE)
    linkedin_url = linkedin_match.group(0) if linkedin_match else None

    github_match = re.search(GITHUB_REGEX, text, re.IGNORECASE)
    github_url = github_match.group(0) if github_match else None

    # Extract city (basic match from predefined list)
    city = extract_city_from_text(lower_text)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "city": city,
        "linkedin_url": linkedin_url,
        "github_url": github_url,
    }
