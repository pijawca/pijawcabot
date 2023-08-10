# -*- coding: utf-8 -*-
#!/usr/bin/env python
import psycopg
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def create_table():
    try:
        conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                cur.execute(
                    f"""CREATE TABLE {DB_NAME} (
                        id serial PRIMARY KEY, 
                        user_id bigint UNIQUE, 
                        username text, 
                        admin int
                        );""")
        except psycopg.errors.DuplicateDatabase:
            pass
    except:
        pass

def check_admins():
    try:
        conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        with conn.cursor() as cur:
            rows = cur.execute(f"SELECT user_id FROM {DB_NAME} WHERE admin=1;")
            rows = cur.fetchall()
            for row in rows:
                user_id = row[0]
                return user_id
    except:
        pass
    
def search_userids():
    try:
        conn = psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        with conn.cursor() as cur:
            rows = cur.execute(f"SELECT user_id FROM {DB_NAME}")
            rows = cur.fetchall()
            for row in rows:
                user_id = row[0]
                return user_id
    except:
        pass
    