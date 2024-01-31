import csv

# Read the csv file
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [row for row in reader]
    return headers, rows

# Write the csv file
def write_csv(filename, headers, rows):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

# Convert strings containing numbers to ints
def convert_to_int(headers, rows):
    for i in range(len(headers)):
        try:
            int(rows[0][i])
            for j in range(len(rows)):
                rows[j][i] = int(rows[j][i])
        except ValueError:
            pass
    return headers, rows

# Calculate the average for each column that contains ints
def calculate_average(headers, rows):
    averages = []
    for i in range(len(headers)):
        try:
            int(rows[0][i])
            total = 0
            for j in range(len(rows)):
                total += rows[j][i]
            average = round(total / len(rows), 2)
            averages.append(average)
        except ValueError:
            averages.append("")
    return averages

# Add the averages as a new row to the csv file
def add_average_to_csv(filename):
    headers, rows = read_csv(filename)
    headers, rows = convert_to_int(headers, rows)
    averages = calculate_average(headers, rows)
    rows.append(averages)
    write_csv(filename, headers, rows)

def lastly(name):
    # Get the name of the csv file from the user
    filename = f'{name}.csv'

    # Add the averages as a new row to the csv file
    add_average_to_csv(filename)

def main(name):
    lastly(name)

if __name__ == '__main__':
    main()
