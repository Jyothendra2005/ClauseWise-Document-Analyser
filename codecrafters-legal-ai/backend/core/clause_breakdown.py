import re

def split_into_clauses(text: str) -> list[str]:
    clauses = re.split(r"\n\s*\n|;|\.\s+", text)
    return [c.strip() for c in clauses if c.strip()]
