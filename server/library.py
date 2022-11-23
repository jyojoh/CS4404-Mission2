import sqlite3 as sql


def checkUser(username, password):
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", (username, password,))
    data = cursor.fetchall()

    if len(data) == 0:
        return False

    return True


def get(user):
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM accounts WHERE username=?", (user,))
    data = cursor.fetchone()
    if data is None:
        return None

    data = cursor.fetchall()

    conn.close()
    return data
