import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

print("Step 1: Loading environment variables...")
load_dotenv()

def get_db_connection():
    try:
        print("Step 2: Establishing database connection...")
        conn = psycopg2.connect(
            host=os.getenv("host"),
            port=os.getenv("port"),
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        print("Database connection established.")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise

try:
    conn = get_db_connection()
    cursor = conn.cursor()
except Exception as e:
    print(f"Exiting due to connection error: {e}")
    exit(1)

def insert_into_db(name, email, message):
    print("Step 3: Storing contact form data...")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact_form (
                detail_id SERIAL PRIMARY KEY,
                name TEXT,
                email TEXT,
                message TEXT 
            )
        """)
        cursor.execute("""
            INSERT INTO contact_form (name, email, message)
            VALUES (%s, %s, %s)
        """, (name, email, message))
        conn.commit()
        print("Data inserted successfully.")
        return {
            "status": "success",
            "message": "Data inserted successfully.",
            "status_code": 200
        }
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
