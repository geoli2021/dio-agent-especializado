"""
app_fixed.py — LABORATÓRIO (versão corrigida)
=============================================

Mesma aplicação de login, agora com consulta parametrizada.
Use este arquivo para validar que a skill orienta a correção correta.
"""

import sqlite3

from flask import Flask, request

app = Flask(__name__)

DB_PATH = "lab.db"


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.execute(
        "INSERT OR IGNORE INTO users VALUES ('admin', 'senha_ficticia')"
    )
    conn.commit()
    conn.close()


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # ✅ SEGURO: consulta parametrizada — o driver trata os valores como dados,
    # nunca como parte da estrutura SQL.
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute(query, (username, password)).fetchone()
    finally:
        conn.close()

    if row:
        return "Login OK"
    return "Falha no login", 401


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="127.0.0.1", port=5000)
