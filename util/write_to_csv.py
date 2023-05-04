import csv
import os

OUTPUT_FOLDER = r'D:\JetBrains\PycharmProjects\PdfTest\data\output'


def PDFToCSVWriter(data_dict):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    csv_path = os.path.join(OUTPUT_FOLDER, 'output.csv')

    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_dict.keys())
        writer.writeheader()
        writer.writerow(data_dict)

    print(f'Output written to {csv_path}')
