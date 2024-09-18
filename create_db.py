import sqlite3

# Connect to SQLite (this will create the file if it doesn't exist)
conn = sqlite3.connect('C:/Users/dell/Desktop/insurance/insurance.db')
cur = conn.cursor()

# SQL query to create the 'project' table
create_table_query = """
CREATE TABLE IF NOT EXISTS project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    gender INTEGER,
    bmi REAL,
    children INTEGER,
    region TEXT,
    smoker INTEGER,
    health INTEGER,
    prediction TEXT
);
"""

# Execute the query to create the table
cur.execute(create_table_query)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Database and 'project' table have been created.")
