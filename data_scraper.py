import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("drivers.db")
cursor = conn.cursor()

# Create table

cursor.execute('''CREATE TABLE IF NOT EXISTS f1_results (year INTEGER, name TEXT, team TEXT, country TEXT, points INTEGER) ''')
