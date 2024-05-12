import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("drivers.db")
cursor = conn.cursor()

# Create table

cursor.execute('''CREATE TABLE IF NOT EXISTS f1_results (year INTEGER, name TEXT, team TEXT, country TEXT, points INTEGER) ''')

# Looping through different years on website 

base_url = "https://www.formula1.com/en/results.html" 

for year in range(2024, 1949, -1):
    url = f"{base_url}/{year}/drivers.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    html_content = response.text #fetching html content from website (for each year)

    soup = BeautifulSoup(html_content, "html5lib")

    table = soup.find("table", class_ = "resultsarchive-table")
    header = soup.find("h1", class_ = "ResultsArchiveTitle")

    year = (header.text.strip())
    names_list = []
    teams_list = []
    country_list = []
    points_list = []

    dict_list = [] # Main output (per year)

    if table:
        tbody = table.find("tbody")
        if tbody:
            rows = tbody.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                for cell in cells:
                    f_names = cell.find("span", class_ = "hide-for-tablet")
                    l_names = cell.find("span", class_ = "hide-for-mobile")
                    team = cell.find("a", class_ = "grey semi-bold uppercase ArchiveLink")

                    if "dark" in cell.get("class", []) and "semi-bold" in cell.get("class", []) and "uppercase" in cell.get("class", []):
                        country = cell.text
                        country_list.append(country)

                    if "dark" in cell.get("class", []) and "bold" in cell.get("class", []):
                        points = cell.text
                        points_list.append(points)

                    if f_names and l_names:
                        # print(f_names.get_text() + " " + l_names.get_text())
                        names_list.append(f_names.get_text() + " " + l_names.get_text())

                    if team:
                        teams_list.append(team.get_text())


    for x in range (len(names_list)):
        dict_list.append({"year": year, "name": names_list[x], "team": teams_list[x], "country": country_list[x], "points": points_list[x]}
)
    print(dict_list)

    for entry in dict_list:
        cursor.execute('''INSERT INTO f1_results (year, name, team, country, points) 
                       VALUES (?,?,?,?,?)''', 
                       (entry["year"], entry["name"], entry["team"], entry["country"], entry["points"])
                       )