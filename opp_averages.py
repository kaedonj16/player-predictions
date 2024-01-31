import csv
import pandas as pd
import player_averages
import player_data
import lastgames
import os

def get_averages_against_opp(csv_file, opp):
    data = []
    last_games = []
    fantasy = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            if row[headers.index("Opp")] == opp:
                data.append([int(cell) if cell.isdigit() else cell for cell in row])
                last_games.append([int(cell) if cell.isdigit() else cell for cell in row])
        for col in range(headers):
            if col <= 8:
                fantasy.append(headers[col])
    averages = []
    for i in range(len(headers)):
        column = [row[i] for row in data]
        if isinstance(column[0], int):
            average = round(sum(column) / len(column), 2)
            averages.append(average)
        else:
            averages.append(headers[i])
    return averages, last_games, fantasy

def opponent(csv_file, answer, name):
    averages, last_games = get_averages_against_opp(csv_file, answer)
    print("Here are " + name + "'s stats against " + answer + " this season:")
    print(["Opp", "FG", "FGA", "%", "3P", "3PA", "%", "TO", "BLK", "STL", "AST", "RB", "PTS", "FS"])
    for i in last_games:
        print(i)
    print(averages)

def lastx(csv_file, answer, name):
    answer = answer.split()
    answer = int(answer[1])
    print("Here are " + name + "'s stats over the last " + str(answer) + " games:")
    print(["Opp", "FG", "FGA", "%", "3P", "3PA", "%", "TO", "BLK", "STL", "AST", "RB", "PTS", "FS"])
    lastgames.main(csv_file, answer)

def predict(csv_file, answer, name):
    data = pd.read_csv(csv_file)
    for row in data:
        if data[data["Opp"]] == answer:
            data.drop(row)
    columns = ["Opp", "FG", "FGA", "3P", "3PA", "TOV", "BLK", "STL", "AST", "TRB", "PTS", "FS"]
    new_data = data[columns]
    new_data.to_csv(f"{name}.csv", index=False) 
    player_data.float_to_percentage(csv_file, [4, 7], 1)

def main():
    name = input("\nEnter the name of the player: ")
    player_data.main(name)
    player_averages.main(name)
    csv_file = f"{name}.csv"
    answer = input("\nPlayer stats - last stretch of games or versus a specific team? \nPlease enter 'Last (Number of Games)' or Opponent 3 letter abbreviation: ")
    print("\n")
    if len(answer) == 3:
        opponent(csv_file, answer, name)
    else: 
        lastx(csv_file, answer, name)

    file_path = f"/Users/kaedonj/Desktop/Misc./Predictions/{name}.csv"

    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
    main()
