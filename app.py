from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"PostgreSQL працює: {version[0]}"
    except Exception as e:
        return f"Помилка підключення до PostgreSQL: {e}"

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5001, debug=True)
