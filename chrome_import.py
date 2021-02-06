import csv, sys
try:
    filename = sys.argv[1]
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        info_store = ''
        for row in reader:
                info = row[0].split(',')
                print(info)
                info = filter(lambda x : 'http' not in x, info)
                info_store += '    '.join(info) + '\n'


        with open('passwords.txt', 'w') as passfile:
                passfile.write(info_store)

except IndexError:
        print('No args passed')

except FileNotFoundError:
        print('File does not exist')
