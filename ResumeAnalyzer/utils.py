"""Utility functions used across modules."""
import re
from typing import Optional

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"\+?\d[\d \-()]{7,}\d")

def extract_email(text: str) -> Optional[str]:
    m = EMAIL_RE.search(text)
    return m.group(0) if m else None

def extract_phone(text: str) -> Optional[str]:
    m = PHONE_RE.search(text)
    return m.group(0) if m else None

def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip()
