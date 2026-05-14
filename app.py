from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "testdb"),
        port=3306
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT)")
            cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            return f"Error: {e}"

    # Fetch all messages
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages")
        messages = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    except Exception as e:
        messages = [f"Error fetching data: {e}"]

    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)   
