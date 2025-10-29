
from Db_connection import connect_to_db, close_connection
from psycopg2.extras import execute_values

# Inserts jobs and skills from dataframe into Postgres.
def load_data_into_db(df):
    """Insert jobs and skills from dataframe into Postgres.

    On success this function will commit the transaction and print a
    confirmation message: "data loaded successfully on successful insertion".
    """
    conn, cursor = connect_to_db()

    records = [
        (
            row.title,
            row.job_id,
            row.date_posted,
            row.url,
            row.company_name,
            row.location_name,
            row.location_area,
            row.longitude,
            row.latitude,
            row.description,
        )
        for _idx, row in df.iterrows()
    ]

    # Inserts jobs using ON CONFLICT DO NOTHING
    query = """
    INSERT INTO jobs (title, job_id, date_posted, url, company, location, area, longitude, latitude, description)
    VALUES %s
    ON CONFLICT (job_id) DO NOTHING
    """
    if records:
        execute_values(cursor, query, records)

    # Creates temporary table for skills to make sure no duplicates are inserted
    cursor.execute(
        """
        CREATE TEMP TABLE tmp_skills (
            job_id TEXT,
            skill TEXT
        ) ON COMMIT DROP
        """
    )

    # Flatten skill records; guard against missing `extracted_skills`
    skill_records = []
    for _idx, row in df.iterrows():
        skills = getattr(row, "extracted_skills", None) or []
        for skill in skills:
            skill_records.append((row.job_id, skill))

    if skill_records:
        execute_values(
            cursor,
            """
        INSERT INTO tmp_skills (job_id, skill)
        VALUES %s
        """,
            skill_records,
        )

        # Inserts into permanent skills table, avoids duplicates.
        
        cursor.execute(
            """
            INSERT INTO skills (job_id, skill)
            SELECT t.job_id, t.skill
            FROM tmp_skills t
            WHERE NOT EXISTS (
                SELECT 1 FROM skills s WHERE s.job_id = t.job_id AND s.skill = t.skill
            )
            """
        )

    conn.commit()

    # Closes connections
    close_connection(conn, cursor)

    print("data loaded successfully on successful insertion")




