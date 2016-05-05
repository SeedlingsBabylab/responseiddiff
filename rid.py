import csv
import sys

old_csvs = []

def get_resp_ids(path):
    with open(path, "rU") as input:
        reader = csv.reader(input)
        reader.next()
        response_ids = [row[0] for row in reader]

        return response_ids

if __name__ == "__main__":

    latest_csv = sys.argv[1]
    old_csvs += sys.argv[2:]

    old_response_ids = []

    for file in old_csvs:
        old_response_ids += get_resp_ids(file)

    with open(latest_csv, "rU") as input:
        with open("diff.csv", "wb") as output:

            reader = csv.reader(input)
            header = reader.next()

            writer = csv.writer(output)
            writer.writerow(header)

            for row in reader:
                if row[0] not in old_response_ids:
                    writer.writerow(row)





