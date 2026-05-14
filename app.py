from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host=os.environ.get("DB_HOST"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"),
                database=os.environ.get("DB_NAME"),
                port=3306
            )
            print("✅ Connected to MySQL!")
            return conn
        except Exception as e:
            print(f"❌ DB Connection failed: {e}, retrying in 5s...")
            time.sleep(5)   

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Connected to MySQL DB!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
