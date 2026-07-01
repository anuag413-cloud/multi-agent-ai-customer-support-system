import sqlite3

conn = sqlite3.connect("support.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT,
query TEXT,
category TEXT,
sentiment TEXT,
priority TEXT,
status TEXT
)
""")

conn.commit()

def create_ticket(customer_name, query, category,
                  sentiment, priority):

    cursor.execute("""
    INSERT INTO tickets
    (customer_name, query, category,
    sentiment, priority, status)

    VALUES(?,?,?,?,?,?)
    """,
    (customer_name,
     query,
     category,
     sentiment,
     priority,
     "Open"))

    conn.commit()


def get_tickets():
    cursor.execute("SELECT * FROM tickets")
    return cursor.fetchall()


def update_ticket_status(ticket_id, status):
    cursor.execute(
        "UPDATE tickets SET status=? WHERE id=?",
        (status, ticket_id)
    )
    conn.commit()