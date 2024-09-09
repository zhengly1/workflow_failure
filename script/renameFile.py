import csv
import shutil

input_csv_file = '../data/data_with_id.csv'

csv_file_path = '../data/data_with_id.csv'

with open(csv_file_path, encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        file_path = 'java/'+row[1].replace("/", "__")+ '/' + str(row[2]) + '_' + str(row[3]) + '_logs.txt'
        target_file_path = 'newjava/'+str(row[0])+'.txt'
        shutil.copyfile(file_path, target_file_path)

        print(f'The file has been copied and renamed {target_file_path}')
