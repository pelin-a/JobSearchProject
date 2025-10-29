# Install flashtext if not already installed:
# pip install flashtext

from flashtext import KeywordProcessor
from typing import List
from skills_list import get_skills_list, get_aliases

# Extracts skills from job descriptions using exact mentions + aliases and returns a list of unique skills found.
def extract_skills(description: str) -> List[str]:
    """
    
     canonical aliases are defined inside the function.
    """
    # get skills list from skills_list module
    skills_list = get_skills_list() 
    
    #get canonical aliases from skills_list module
    canonical_aliases = get_aliases()

    # adds skills and aliases to keyword processor that handles case insensitivity and mapping
    kp = KeywordProcessor(case_sensitive=False)
    for skill in skills_list:
        kp.add_keyword(skill)
    for alias, canonical in canonical_aliases.items():
        kp.add_keyword(alias, canonical)

    # extracts matches
    matches = kp.extract_keywords(description)

    # Removes duplicates while preserving order
    seen = set()
    unique_matches = []
    for m in matches:
        if m not in seen:
            unique_matches.append(m)
            seen.add(m)
    
    return unique_matches

# test example
if __name__ == '__main__':
    job_description = """
    We are looking for a motivated, technically curious student.
    Strong programming skills in Python (experience with pandas, SQLAlchemy, or requests a plus).
    First-hand experience with databases (SQL or NoSQL) and basic data modeling.
    Interest or prior exposure to ETL tools, APIs, or data pipeline frameworks.
    Familiarity with cloud environments (AWS, GCP, or similar) and Docker is a plus—not a requirement.
    """
    
    skills_found = extract_skills(job_description)
    print(skills_found)
