#https://api.adzuna.com/v1/api/jobs/de/search/2?app_id=fbc16ca1&app_key=7d40e32150a6eac4c4f0e7008f52bc5e&results_per_page=50&what=data+intern&where=Deutschland
import os
import requests
import json
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# gets job data using adzuna api, api id and api key are stored in environment variables for security reasons.
# returns list of job postings in json format
def fetch_jobs(n):
    app_id = os.getenv('API_ID')
    app_key = os.getenv('API_KEY')  
    if not app_id or not app_key:
        raise ValueError("API_ID and API_KEY must be set in environment variables")
    
    page_number=n
    results_per_page=100
    what="data intern"
    where="Deutschland"
    url = f"https://api.adzuna.com/v1/api/jobs/de/search/{page_number}?app_id={app_id}&app_key={app_key}&results_per_page={results_per_page}&what={what}&where={where}&sort_by=date"
    
    try:
        response= requests.get(url)
        response.raise_for_status()
        data=response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []    
    
    return data.get('results', [])

# keys= dict_keys(['__CLASS__', 'id', 'salary_is_predicted', 'title', 'description', 'contract_time', 'company', 'created', 'category', 'location', 'redirect_url', 'adref'])




