import sqlite3 as sql


def checkUser(username, password):
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", (username, password,))
    data = cursor.fetchall()
    conn.close()

    if len(data) == 0:
        return False

    return True


def get_phone_host(user):
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM accounts WHERE username=?", (user,))
    data = cursor.fetchone()
    conn.close()
    
    if data is None:
        return None

    return data[0]
