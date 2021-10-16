import csv, sys
from encryption import EncryptionService
from utils import navigate_to_store

class IngestionService:
        def __init__(self, password):
                self.encrypter = EncryptionService(password)

        def csv_import(self, filename):
                """For importing passwords from browser based password managers"""
                try:
                        with open(filename, newline='') as csvfile:
                                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                                info_store = ''
                                for row in reader:
                                        info = row[0].split(',')
                                        info[-1] = str(self.encrypter.encrypt(info[-1]))
                                        del info[1] #remove url, site name at idx 0
                                        print(info)
                        
                                        info_store += '    '.join(info) + '\n'

                                navigate_to_store()
                                with open('store', 'w') as passfile:
                                        passfile.write(info_store)

                except FileNotFoundError:
                        print('File does not exist')



