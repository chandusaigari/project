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
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # Insert example data
            cursor.execute("INSERT INTO test_table (message) VALUES (%s)", [request.form["message"]])
            conn.commit()
            cursor.close()
            conn.close()
            return "Data inserted successfully!"
        except Exception as e:
            return f"Insert failed: {e}"

    # Render a simple form
    return '''
    <h1>Connected to MySQL DB!</h1>
    <form method="POST">
        <input type="text" name="message" placeholder="Enter something" required />
        <button type="submit">Insert Data</button>
    </form>
    '''   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
