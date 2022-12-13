import sqlite3

# establishes connection to database
conn = sqlite3.connect("jetliners.sqlite")

# cursor object used to execute SQL statements
# creating table

cursor = conn.cursor()
sql_query = """ CREATE TABLE jetliners (
    id integer PRIMARY KEY,
    type text NOT NULL,
    origin text NOT NULL,
    engines integer, 
    first_flight text NOT NULL,
    service_entry text NOT NULL,
    in_production text NOT NULL,
    inventory int NOT NULL
)"""

cursor.execute(sql_query)
