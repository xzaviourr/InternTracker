import psycopg2
from connection import obj
from logger import db_logger

tables = [
    """
    CREATE TABLE IF NOT EXISTS Alumni (
        Alumni_id SERIAL PRIMARY KEY,
        Linkedin_url VARCHAR,
        Year VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Companies (
        Company_id SERIAL PRIMARY KEY,
        Name VARCHAR,
        Stipend_min INTEGER,
        Stipend_max INTEGER,
        Company_level INTEGER
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Users (
        User_id SERIAL PRIMARY KEY,
        Name VARCHAR,
        Password VARCHAR,
        Email VARCHAR,
        Phone VARCHAR,
        Year VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Internships (
        Internship_id SERIAL PRIMARY KEY,
        Company_name VARCHAR,
        Start_date VARCHAR,
        Deadline VARCHAR,
        Stipend_min INTEGER,
        Stipend_max INTEGER,
        Number_of_applicants INTEGER,
        Posting_date VARCHAR,
        Role VARCHAR,
        Category_id INTEGER,
        Link VARCHAR,
        Location VARCHAR
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Skills (
        Skill_id SERIAL PRIMARY KEY,
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

try :

    conn = obj.connect()

    cur = conn.cursor()

    for table in tables :
        cur.execute(table)

    cur.close()

    conn.commit()

    conn.close()

except :

    db_logger.error("Error in connection to database")