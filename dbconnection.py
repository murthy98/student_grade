import psycopg2
import os
def connection():
    db = f"dbname={os.getenv('DATABASE')} user={os.getenv('USER')} password={os.getenv('PASSWORD')} host={os.getenv('HOST')}"
    #conn=psycopg2.connect(database='d3aooc4t84kn0n' ,user='cdzgrdnckdgqjw' ,password='032ea1b1f89bb5b4d594fe27e510b10531ebaee8bd3d4f0947c8297bcecdca14' ,host='ec2-23-21-186-85.compute-1.amazonaws.com')
    conn = psycopg2.connect(db)
    c = conn.cursor()
    return c, conn
