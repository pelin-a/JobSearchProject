#TODO: create a db and connect, 
#TODO: write your steps from the beginning to the end
import psycopg2
import os
#connects to the database using credentials from environment variables, returns connection and cursor
def connect_to_db():
    try:
        conn = psycopg2.connect(database = "jobs_db", 
                        user = os.environ.get('db_user'),
                        password = os.environ.get('db_password'),
                        host= 'localhost',
                        port = 5432)
        cursor = conn.cursor()
        print("Database connected successfully")
        return conn, cursor
    except Exception as e:
        print("Error while connecting to database", e)
        return None, None
    
conn, cursor = connect_to_db() 

# Closes the database connection
def close_connection(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed")

# Executes a given SQL query with optional parameters
def execute_query(conn, query, params=None):
    if not conn:
        print("No database connection")
        return None
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        print("Query executed successfully")
    except Exception as e:
        print("Error executing query", e)
        conn.rollback()  
    cursor.close()
    
# Fetches data from the database based on a query and optional parameters
def fetch_query(conn, query, params=None):
    if not conn:
        print("No database connection")
        return None
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error fetching data", e)
        return None
    finally:
        cursor.close()

# Creates jobs and skills tables if they do not exist       
def create_tables():
    conn, cursor = connect_to_db()
    if not conn or not cursor:
        return

    job_table_query = """ CREATE TABLE IF NOT EXISTS jobs (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        job_id VARCHAR(100) UNIQUE NOT NULL,
        date_posted DATE,
        url TEXT,
        company VARCHAR(255),
        location VARCHAR(255),
        area VARCHAR(100),
        longitude FLOAT,
        latitude FLOAT,
        description TEXT);"""

    skills_table_query = """ CREATE TABLE IF NOT EXISTS skills (
    job_id VARCHAR(100) NOT NULL REFERENCES jobs(job_id),
    skill VARCHAR(100) NOT NULL);"""

    execute_query(conn, job_table_query)
    execute_query(conn, skills_table_query)
    close_connection(conn, cursor)

