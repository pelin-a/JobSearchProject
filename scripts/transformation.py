#%%
import pandas as pd
import fetch_jobs
import json
from skill_extraction import extract_skills
from scrape_description import scrape_job_description


# %%
# Loads job data from fetch_jobs.py and normalizes it into a pandas DataFrame
def load_data(n): #loads data from fetch_jobs.py
    data = fetch_jobs.fetch_jobs(n)
    df = pd.json_normalize(data)
    return df  

# %%
# Drops unnecessary columns from the dataframe
def drop_columns(df_raw): #drops unnecessary columns
    df=df_raw.copy()
    df=df.drop(columns=['salary_is_predicted', '__CLASS__', 'adref','contract_time', 'description',
                        'category.__CLASS__','category.label','location.__CLASS__','category.tag','company.__CLASS__','contract_type'])
    return df
    
    
# %%
# Renames columns to more user friendly names
def rename_columns(df): #renames columns to more user friendly names
    df=df.rename(columns={'created':'date_posted','company.display_name':'company_name','id':'job_id',
                          'location.area':'location_area','location.display_name':'location_name','redirect_url':'url'})
    
    return df


#%%
# Adds full job descriptions by scraping the job posting url
def add_job_descriptions(df): #adds full job descriptions by scraping the job posting url
    df['description'] = df['url'].apply(lambda url: scrape_job_description(url))
    return df


# %%
# Changes data types of columns to more suitable types
def change_dtypes(df): #changes data types of columns from object to more suitable types
    df['date_posted']=pd.to_datetime(df['date_posted'])
    df['location_area'] = df['location_area'].astype('string')  # or .astype(str)
    df['location_area'] = df['location_area'].str.strip('[]').str.split(',')
    df['location_area'] = df['location_area'].apply(lambda x: [i.strip() for i in x] if isinstance(x, list) else [])
    df['location_area'] = df['location_area'].apply(lambda x: x[0].strip(" '\"") if len(x) > 0 else None)
    df[['title','job_id','description','company_name','location_name']]=df[['title','job_id','description','company_name','location_name']].astype('string')
    return df

# %%
# Adds extracted skills to the dataframe using skill_extraction.py
def add_extracted_skills(df):
    df = df.copy()
    df['extracted_skills'] = df['description'].apply(lambda desc: extract_skills(desc))
    return df
# %%
#TODO: automate process for every time api is called, only new jobs should be added to db, add only necessary columns to db.
# Transforms the dataframe by applying all transformation functions
def transform_data(df):
    df=drop_columns(df)
    df=rename_columns(df)
    df= add_job_descriptions(df)
    df=change_dtypes(df)
    df=add_extracted_skills(df)
    return df


# %%
# Example usage
df0 = load_data()
df= transform_data(df0)
df.head()
#%%
df['extracted_skills'].head()

