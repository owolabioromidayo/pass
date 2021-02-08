## pass - A minimalistic, terminal based password manager

## Why Pass
* Easy Storage and Retrieval of Passwords
* Persistence with Github
* Privacy & Security with sudo and chmod 

## Setup
1. clone this repo ```git clone https://github.com/owolabioromidayo/pass``` 

1. edit your terminal config
	in zsh -> ```alias pass="python3 pathtopass/pass/pass.py"```
	
1. edit config PASS_DIR setting to chosen absolute path to pass in your system

1. export passwords from browser to pass dir and run ```python3 chrome_import.py passwords_filename.csv```

1. create a private git repo for storage and push to it

1. use pass commit to push changes to github, changes such as adding and removal of passwords auto commit and just need to be 
pushed with pass commit.

1. you can make your passwords inaccessible to others using your computer without root access by using ```sudo chmod 000 pathtopass```
when not in use then ```sudo chmod 777 pathtopass``` so that you have a master key to your passwords. You can even make these aliases
in your terminal of choice

## How To Use
* ```pass add info1 info2 ...``` i.e ```pass add google.com mailaddress@gmail.com ``` <br />
 adds info1 info2 ...  to password file

* ```pass find info``` <br />
  prints all lines in password storage which contain info
  
* ```pass gen info1 info2 ...``` i.e ```pass gen google.com mailaddress@gmail.com ``` <br />
 generates a password and adds info1 info2 ... + generated_password to password file

* ```pass remove info ``` <br />
  prompts for deletion of each line that contains info
 

* ```pass commit``` <br />
  commit changes if any and pushes to private github repo if configured
 



## Extra Tips
* Comment out lines in your config file with #

## Enjoy!
