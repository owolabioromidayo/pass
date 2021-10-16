import os,sys, random, subprocess

from config import ConfigService

from encryption import EncryptionService
from ingestion import IngestionService
from auth import AuthenticationService
from persistence import GitPersistenceService
from utils import navigate_to_store


class TextInterface:
    def __init__(self):
        self.actions = {
            'add': self.add, 
            'gen': self.generate_password, 
            'find':self.find, 
            'remove':self.remove, 
            'commit':self.commit
            }

        self.config = ConfigService()
        

def add(self, args):
        print('Adding')
        with open('store', 'a') as passfile:
                info  =  '   '.join(args)
                passfile.write(f"\n {info}")
                print(f"{info} added!")


def generate_password(self, args):
        chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;:.,?/|~`!@#$%^&*_-+=")
        password = ""
        for _ in range(random.choice(range(15, 21))):
                password += random.choice(chars)
        print(password)
        args.append(password)
        add(args)       


def find(self, args):
        with open('store', 'r') as passfile:
                for line in passfile.readlines():
                        info =  line.split('   ')
                        if len(list(filter(lambda x: args[0] in x, info))):
                                        print('   '.join(info).strip())  


def remove(self, args):
        lines = []
        removeIdx  = []
        with open('store', 'r') as passfile:
                lines = passfile.readlines()

        with open('store', 'w') as passfile:
                for line in lines:
                        info =  line.split('   ')
                        if len(list(filter(lambda x: args[0] in x, info))):
                                confirm = input(f"Do you want to delete field {'   '.join(info).strip()}  (y/n)  ? ")
                                if confirm == 'y':
                                        removeIdx.append(line)  
                                        print(f"{'   '.join(info).strip()} deleted")                    
                                        
                for line in lines:
                    if line not in removeIdx:
                        passfile.write(line)


def commit(self, args):
            os.system('git add . && git commit -m "update" ')
            os.system('git push origin master')


def main(self):
    navigate_to_store()

    try:
        action = sys.argv[1]
        args = []
        if len(sys.argv) > 2:
                args = sys.argv[2:]
    
        if action in actions:
            actions[action](args)
            if action != 'find':
                os.system('git add . && git commit -m "update" ')
        else:
            print('Action not supported')

    except IndexError:
            print('Not enough args')

    except Exception as err:
            print(f"An exception occured {err}")

