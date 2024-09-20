import psycopg2
from psycopg2 import sql
from typing import List, Tuple, Any
import os

db_params = {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432")
    }

def ejecutar_sql(sql_command: str, params: list= []) -> List[Tuple[Any, ...]]:
    try:
        with psycopg2.connect(**db_params) as conn:
            with conn.cursor() as cur:
                if params:
                    cur.execute(sql_command, params)
                else:
                    cur.execute(sql_command)
                if cur.description:
                    results = cur.fetchall()
                else:
                    results = [(cur.rowcount,)]
                conn.commit()
        return results
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []