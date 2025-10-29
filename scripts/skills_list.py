# returns a list of skills 
def get_skills_list():

    skills_list = [
    # Programming languages
    "Python", "R", "SQL", "VBA", "SAS", "MATLAB", "JavaScript",

    # Data manipulation & analysis
    "Pandas", "NumPy", "SciPy", "Scikit-learn", "Statsmodels", "Data Analysis", "Data Wrangling", "Data Cleaning",
    "Data Mining", "Data Modeling", "ETL", "Workflow Automation",

    # Machine learning & AI
    "Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision",
    "Predictive Modeling", "Reinforcement Learning", "AI", "ML Ops", "Transfer Learning", "Feature Engineering",
    
    # Deep learning frameworks
    "TensorFlow", "Keras", "PyTorch", "FastAI", "Hugging Face Transformers",
    
    # Big data & distributed computing
    "Hadoop", "Spark", "Databricks", "Airflow", "Data Warehousing", "Snowflake",
    
    # Cloud platforms
    "AWS", "Azure", "GCP", "Cloud Computing", "Serverless",
    
    # Databases
    "PostgreSQL", "MySQL", "MongoDB", "Oracle", "Redshift", "BigQuery", "NoSQL",
    
    # Business intelligence & visualization
    "Excel", "Power BI", "Tableau", "Looker", "Looker Studio", "Data Visualization",
    "Matplotlib", "Seaborn", "Plotly", "Dash", "QlikView", "Google Data Studio",
    
    # DevOps & collaboration tools
    "Git", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Agile", "Scrum", "JIRA",
    
    # Statistics & math
    "Statistics", "Probability", "Hypothesis Testing", "A/B Testing", "Optimization", "Linear Algebra", "Calculus",
    
    # Data communication / business skills
    "Reporting", "Dashboarding", "Business Intelligence", "Storytelling", "Data-driven Decision Making",
    
    # Misc / Other relevant skills
    "APIs", "REST API", "GraphQL", "Data Quality", "Data Governance", "SQL Server", "Google BigQuery",
    "Workflow Automation Tools", "Zapier", "Alteryx"
    ]
    return skills_list
#returns a dictionary of aliases mapping to canonical skill names
def get_aliases():
    aliases = {
        'ml': 'Machine Learning',
        'pd': 'Pandas',
        'np': 'NumPy',
        'sklearn': 'Scikit-learn',
        'scikit': 'Scikit-learn',
        'data analytics': 'Data Analysis',
        'analytics': 'Data Analysis',
        'tf': 'TensorFlow',
        'tensorflow': 'TensorFlow',
        'pytorch': 'PyTorch',
        'postgre': 'PostgreSQL',
        'postgres': 'PostgreSQL',
        'psql': 'PostgreSQL',
        'pg': 'PostgreSQL',
        'mysql': 'MySQL',
        'mongo': 'MongoDB',
        'mongodb': 'MongoDB',
        'snowflake': 'Snowflake',
        'databricks': 'Databricks',
        'dbt': 'Databricks',
        'aws': 'AWS',
        'amazon web services': 'AWS',
        'azure': 'Azure',
        'gcp': 'GCP',
        'powerbi': 'Power BI',
        'power-bi': 'Power BI',
        'tableau': 'Tableau',
        'hubspot': 'Business Intelligence',
        'looker': 'Business Intelligence',
        'looker studio': 'Business Intelligence',
        'nlp': 'Natural Language Processing',
        'etl': 'ETL',
        'airflow': 'Airflow',
        'docker':  'Docker',
    }
    return aliases