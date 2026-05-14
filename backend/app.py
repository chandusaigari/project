from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "appuser"),
        password=os.environ.get("DB_PASSWORD", "apppass"),
        port=os.environ.get("DB_PORT", "5432")
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.before_first_request
def setup():
    init_db()

# CREATE
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, name, email, created_at",
            (data["name"], data["email"])
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": row[0], "name": row[1], "email": row[2], "created_at": str(row[3])}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ ALL
@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, created_at FROM users ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        users = [{"id": r[0], "name": r[1], "email": r[2], "created_at": str(r[3])} for r in rows]
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ ONE
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, created_at FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"id": row[0], "name": row[1], "email": row[2], "created_at": str(row[3])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# UPDATE
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET name=%s, email=%s WHERE id=%s RETURNING id, name, email, created_at",
            (data["name"], data["email"], user_id)
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if not row:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"id": row[0], "name": row[1], "email": row[2], "created_at": str(row[3])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id=%s RETURNING id", (user_id,))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if not row:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": f"User {user_id} deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# HEALTH CHECK
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)