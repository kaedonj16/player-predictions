import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Request the website and parse the HTML content
def get_player_stats(username):
    url = f"https://www.basketball-reference.com/players/{username}/gamelog/2023"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the table containing the player's stats
    table = soup.find("table", {"id":"pgl_basic"})
    
    # Get the first row containing the headers
    headers = [header.text for header in table.find_all("th")]
    headers = headers[1:30]
    
    # Get the rows containing the player's stats
    rows = []
    for row in table.find_all("tr")[0:]:
        cells = [cell.text for cell in row.find_all("td")]
        if cells:
            if cells[0] != '':
                rows.append(cells)
    
    # Return the headers and the rows
    return headers, rows

# Save the player's stats into a csv file
def save_to_csv(name, headers, rows):
    filename = f"{name}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    data = pd.read_csv(filename)
    columns = ["G", "Opp", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "TOV", "BLK", "STL", "AST", "TRB", "PTS"]
    new_data = data[columns]
    new_data.to_csv(f"{name}.csv", index=False) 
    float_to_percentage(filename, [4, 7], 1) 
    return filename

def float_to_percentage(file_name, columns, decimal_places):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [row for row in reader]
    
    for row in rows:
        for column in columns:
            if row[column] != '':
                value = float(row[column])
                percentage = round(value * 100, decimal_places)
                row[column] = "{}%".format(percentage)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    
def calculate_fantasy_score(csv_path):
    # Load the data into a pandas dataframe
    df = pd.read_csv(csv_path)

    # Calculate the fantasy score using a formula
    fantasy_score = df['PTS'] + (1.2 * df['TRB']) + (1.5 * df['AST']) + (3 * df['STL']) + (3 * df['BLK']) - (df['TOV'])

    # Add the new column to the dataframe
    df['Fantasy Score'] = fantasy_score
    df = df.rename(columns={'Fantasy Score': 'FS'})
    df['FS'] = df['FS'].astype(int)

    # Save the dataframe back to the CSV
    df.to_csv(csv_path, index=False)


def lastly(name):
    # Get the name of the player from the user
    splitname = name.split()
    firstname = splitname[0]
    lastname = splitname[1]
    username = lastname[0]+ "/" + lastname[0:5] + firstname[0:2] + "01"

    # Get the player's stats and save it into a csv file
    headers, rows = get_player_stats(username.lower())
    csv_file = save_to_csv(name, headers, rows)
    calculate_fantasy_score(csv_file)


def main(name):
    lastly(name)

if __name__ == '__main__':
    main()