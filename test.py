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



# # EXPORTING DATA OF SQLITE DATABASE TO TXT FILE

# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect("drivers.db")
# cursor = conn.cursor()

# # Execute an SQL SELECT query to retrieve all rows from the table
# cursor.execute("SELECT * FROM f1_results")

# # Fetch all rows from the result set
# rows = cursor.fetchall()

# # Write the contents to a text file
# with open("f1_results.txt", "w") as f:
#     # Write column names
#     f.write("Year | Name | Team | Country | Points\n")
    
#     # Write each row of the result set
#     for row in rows:
#         f.write(" | ".join(str(cell) for cell in row) + "\n")

# # Close cursor and connection
# cursor.close()
# conn.close()

# PRINTING TABLE

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("drivers.db")
cursor = conn.cursor()

# Execute an SQL SELECT query to retrieve all rows from the table
cursor.execute("SELECT * FROM f1_results")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the column names
print("Year | Name | Team | Country | Points")

# Print each row of the result set
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()