import random
import csv

all_numbers = list(range(1, 15355))

random_numbers = random.sample(all_numbers, 375)


with open('../data/data_with_id.csv', 'r', encoding='utf-8') as input_file, open('../data/data.csv', 'w', newline='', encoding='utf-8') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    header = next(csv_reader)
    csv_writer.writerow(header)

    for row in csv_reader:
        if row[0].isdigit() and int(row[0]) in random_numbers:
            csv_writer.writerow(row)



