# 🧠 Job Market Skill Extraction & Analysis

An end-to-end **ETL pipeline** that automatically fetches job postings, scrapes full descriptions, extracts relevant **skills using NLP-based matching**, stores the data in a **PostgreSQL database**, and visualizes trends in the most in-demand skills and top employers.


 # Features

Job scraping from Adzuna job listings
Skill extraction using keyword and alias matching (with FlashText)
Data storage in PostgreSQL
Duplicate-safe incremental loading (only inserts new records)
Data analysis & visualization, including:
Most demanded skills
Top employers by job count

---

## 🚀 Project Overview

This project automates the process of analyzing the job market for data-related roles.  
It fetches job data from the **Adzuna API**, extracts and cleans job descriptions, identifies required technical skills, and stores the data in a relational database for visualization and analysis.

---

## 🧩 Pipeline Summary

| Step | Module | Description |
|------|---------|-------------|
| **1. Fetch Jobs** | `fetch_jobs.py` | Fetches raw job data from the Adzuna API. |
| **2. Define Skills** | `skills.py` | Provides skill lists and aliases for extraction. |
| **3. Scrape Descriptions** | `scrape_description.py` | Scrapes full job descriptions from the job URLs using BeautifulSoup. |
| **4. Extract Skills** | `skill_extraction.py` | Uses FlashText to detect skills and aliases within job descriptions. |
| **5. Transform Data** | `transformation.py` | Cleans, formats, and adds extracted skills using modular transformation functions. |
| **6. Database Connection** | `db_connection.py` | Manages PostgreSQL connections and disconnections. |
| **7. Load to Database** | `load.py` | Inserts cleaned job and skill data into PostgreSQL (`jobs` and `skills` tables). |
| **8. ETL Orchestration** | `ETL.py` | Runs extract, transform, and load steps in sequence for easy automation. |
| **9. Data Analysis** | `analysis.ipynb` | Visualizes top skills, top employers, and calculates average number of skills per job. |

---

## 🧱 Folder Structure
project/
│
├────scripts/
├── fetch_jobs.py
├── skills.py
├── scrape_description.py
├── skill_extraction.py
├── transformation.py
├── db_connection.py
├── load.py
├── ETL.py
├──── visualisations/ 
├── analysis.ipynb
└────  requirements.txt

## Technologies Used

Python 3.10+
BeautifulSoup4
FlashText
Pandas
psycopg2
PostgreSQL
Matplotlib / Seaborn

## Future Improvements

Add skill co-occurrence heatmaps would be beneficial to see what skills are better when learned together.
Implement time-based trend analysis for emerging skills (requires enough time to see the trends).
Deploy as an automated daily ETL job using Airflow or Cron. 

Pelinsu Altun - Potsdam, Germany
