from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import time

app = Flask(__name__)

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "123"),
        database=os.getenv("DB_NAME", "db"),
        port=3306
    )

# Initialize Database
def init_db():
    for i in range(10):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    message TEXT
                )
            """)

            conn.commit()
            cursor.close()
            conn.close()

            print("✅ Database initialized")
            return

        except Exception as e:
            print(f"⏳ Waiting for MySQL... {e}")
            time.sleep(5)

    print("❌ Could not connect to MySQL")

with app.app_context():
    init_db()

# Home Page
@app.route("/", methods=["GET", "POST"])
def index():

    # Add Message
    if request.method == "POST":
        message = request.form["message"]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO messages (message) VALUES (%s)",
                (message,)
            )

            conn.commit()

            cursor.close()
            conn.close()

        except Exception as e:
            return f"Insert Error: {e}"

    # Fetch Messages
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, message FROM messages")

        messages = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        messages = [(0, f"Fetch Error: {e}")]

    return render_template("index.html", messages=messages)

# Delete Message
@app.route("/delete/<int:id>")
def delete_message(id):

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM messages WHERE id=%s",
            (id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        return f"Delete Error: {e}"

    return redirect("/")

# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
