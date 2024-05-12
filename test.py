# CHECK FOR PRESENCE OF TABLE

# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('drivers.db')
# cursor = conn.cursor()

# # Execute an SQL query to list all tables
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# # Fetch all table names from the result set
# tables = cursor.fetchall()

# # Print the list of tables
# print("Tables in the database:")
# for table in tables:
#     print(table[0])

# # Close the cursor and the connection
# cursor.close()
# conn.close()