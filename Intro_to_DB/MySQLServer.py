import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()





# Read values from .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


try:
# Connect to MySQL
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    if conn.is_connected():
        print(" Connected to MySQL Server")
        print(" MySQL version:", conn.get_server_info())

except Error as e:
    print(f" MySQL Connection Error: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print(" Connection closed")
        
