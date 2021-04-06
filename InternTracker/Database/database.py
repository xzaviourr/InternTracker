import psycopg2

conn = psycopg2.connect("dbname = <PLACEHOLDER> user = <PLACEHOLDER> password = <PLACEHOLDER>") # Fill <PLACEHOLDER>'s with values as per respective setups

cur = conn.cursor()

tables = [
    """
    CREATE TABLE IF NOT EXISTS Alumni (
        Alumni_id INTEGER,
        Linkedin_url VARCHAR,
        Year VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Companies (
        Company_id INTEGER,
        Name VARCHAR,
        Stipend_min INTEGER,
        Stipend_max INTEGER,
        Company_level INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Users (
        User_id INTEGER,
        Name VARCHAR,
        Password VARCHAR,
        Email VARCHAR,
        Phone VARCHAR,
        Year VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Internships (
        Internship_id INTEGER,
        Company_id INTEGER,
        Start_date VARCHAR,
        Deadline VARCHAR,
        Stipend INTEGER,
        Number_of_applicants INTEGER,
        Posting_date VARCHAR,
        Role VARCHAR,
        Category_id INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Skills (
        Skill_id INTEGER,
        Skill_name VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS User_Skills (
        User_id INTEGER,
        Skill_id INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS User_company_tracker (
        Company_id INTEGER,
        User_id INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Alumni_company (
        Alumni_id INTEGER,
        Company_id INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Internship_skills (
        Internship_id INTEGER,
        Skills_id INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Categories (
        Category_id INTEGER,
        Category_name VARCHAR
    )
    """
]

for table in tables :
    cur.execute(table)

cur.close()

conn.commit()

conn.close()