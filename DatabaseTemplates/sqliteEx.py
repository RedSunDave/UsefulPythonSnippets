import sqlite3


def create_table():
    # Establish connection and database
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # Create a table named 'store', and add columns
    cur.execute("CREATE TABLE IF NOT EXISTS [tablename] ([variable1-text] TEXT, [variable2-integer] INTEGER, [variable3-test] TEXT)")
    conn.commit()
    conn.close()


def insert(variable1, variable2, variable3):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (variable1, variable2, variable3))
    conn.commit()
    conn.close()


def delete(variable1):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE variable1=?", (variable1,))
    conn.commit()
    conn.close()


def update(variable1, variable2, variable3):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET variable2=?, variable3=? WHERE variable1=?", (variable2, variable3, variable1))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tablename")
    rows = cur.fetchall()
    conn.close()
    return rows

