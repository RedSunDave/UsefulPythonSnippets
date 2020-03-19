#!usr/bin/python3
"""
Creates a simple database table for item, stock quantity, and price
"""
import sqlite3


def create_table():
    # Establish connection and database
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # Create a table named 'store', and add columns
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # Example Item below
    # cur.execute("INSERT INTO store VALUES ('wine Glass', 8, 10.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    """
    Add a new item to the inventory list.
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def delete(item):
    """
    Delete an item from the store inventory list.
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item, ))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    """
    Update the quantity and price of an item in the store
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


def view():
    """
    View the prices for each item in the store
    """
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
