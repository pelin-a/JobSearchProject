import requests
from bs4 import BeautifulSoup
import re

# Function to scrape job description from a given URL
def scrape_job_description(url: str) -> str:
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/117.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Finds the section containing the job description
        section = soup.find("section", class_="adp-body")

        for br in section.find_all("br"):
            br.replace_with("\n")

        # Extracts text
        text = section.get_text(separator="\n", strip=True)

        # Cleans multiple newlines and extra spaces
        cleaned_lines = []
        for line in text.splitlines():
            line = line.strip()
            # Removes leading bullets or dashes
            line = re.sub(r'^[\+\-\•]\s*', '', line)
            if line:
                cleaned_lines.append(line)

        # Joins cleaned lines back into a single string
        cleaned_text = "\n".join(cleaned_lines)
        return cleaned_text
        
    
  
    # Handles exceptions and returns empty string on failure
    except Exception as e:
        print(f" Error scraping {url}: {e}")
        return ""


#TODO: handle + in descriptions