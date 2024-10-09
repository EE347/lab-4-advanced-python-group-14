import csv

def write_names():
    with open('task5.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        while True:
            name = input("Eneter a name or 'quit' to exit: ")
            if name.lower() == 'quit':
                break
            writer.writerow([name])

def read_names():
    with open('task5.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])

if __name__ == '__main__':
    write_names()
    read_names()