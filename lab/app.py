"""
app.py — LABORATÓRIO
====================

Aplicação de login INTENCIONALMENTE VULNERÁVEL a SQL Injection,
usada apenas para testar a skill `vulnerability-analysis` do DIO Agent.

NÃO USE EM PRODUÇÃO. NÃO EXPONHA NA INTERNET.
Execute apenas em ambiente isolado (VM, container local, 127.0.0.1).
"""

import sqlite3

from flask import Flask, request

app = Flask(__name__)

DB_PATH = "lab.db"


def init_db() -> None:
    """Cria a tabela e insere um usuário fictício."""
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

    # ❌ VULNERÁVEL: concatenação direta de entrada do usuário na consulta.
    query = (
        f"SELECT * FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )

    conn = sqlite3.connect(DB_PATH)
    try:
        row = conn.execute(query).fetchone()
    finally:
        conn.close()

    if row:
        return "Login OK"
    return "Falha no login", 401


if __name__ == "__main__":
    init_db()
    # Escuta apenas em localhost — nunca em 0.0.0.0 em laboratório.
    app.run(debug=True, host="127.0.0.1", port=5000)
