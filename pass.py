import os,sys, random

def add(args):
	print('Adding')
	with open('passwords.txt', 'a') as passfile:
		info  =  '   '.join(args)
		passfile.write(info)
		print(f"{info} added!")

def gen(args):
	chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[];:.,<>?/|~`!@#$%^&*()_-+=")
	password = ""
	for _ in range(random.choice(range(15, 21))):
		password += random.choice(chars)
	print(password)
	args.append(password)
	add(args)	


def find(args):
	with open('passwords.txt', 'r') as passfile:
		for line in passfile.readlines():
			info =  line.split('   ')
			for field in info:
				if args[0] in field:
					print('   '.join(info).strip())			
def remove(args):
	lines = []
	with open('passwords.txt', 'r') as passfile:
		lines = passfile.readlines()

	with open('passwords.txt', 'w') as passfile:
		for line in lines:
			info =  line.split('   ')
			for field in info:
				if args[0] in field:
					confirm = input(f"Do you want to delete field {'   '.join(info).strip()}  (y/n)  ? ")
					if confirm == 'y':
						lines.remove(line)
						print(f"{'   '.join(info).strip()} deleted")			

		for line in lines:
			passfile.write(line)


def commit(args):
            os.system('git add . && git commit -m "update" && git push origin master')

def main():
    actions = {'add': add, 'gen':gen, 'find':find, 'remove':remove, 'commit':commit}

    try:
        action = sys.argv[1]
        args = []
        if len(sys.argv) > 2:
                args = sys.argv[2:]
    
        if action in actions:
            actions[action](args)
            os.system('git add . && git commit -m "update" ')
        else:
            print('Action not supported')
    except IndexError:
            print('Not enough args')
    except Exception as err:
	    print(f"An exception occured {err}")


if __name__ == "__main__":
    main()
