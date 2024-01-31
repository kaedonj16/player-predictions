import csv

def get_last_rows(csv_file, input):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append([int(cell) if cell.isdigit() else cell for cell in row])
    return headers, data[-(input+1):-1]

def get_averages(headers, data):
    averages = []
    for i in range(len(headers)):
        column = [row[i] for row in data]
        if isinstance(column[0], int):
            average = round(sum(column) / len(column), 2)
            averages.append(average)
        else:
            averages.append(headers[i])
    return averages

def main(csv_file, input):
    headers, last_games = get_last_rows(csv_file, input)
    averages = get_averages(headers, last_games)
    for i in last_games:
        print(i)
    print(averages)

if __name__ == '__main__':
    main()
