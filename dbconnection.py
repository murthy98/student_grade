import psycopg2
import os
def connection():
    db = f"dbname={os.getenv('DATABASE')} user={os.getenv('USER')} password={os.getenv('PASSWORD')} host={os.getenv('HOST')}"
    conn = psycopg2.connect(db)
    c = conn.cursor()
    return c, conn
