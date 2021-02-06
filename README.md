## A minimalistic, terminal based password manager
A sub 100 line password manager
### How To Use
	clone this repo
	edit zsh -> alias pass="python3 pass/pass.py"
	export passwords from browser to pass dir and run python3 chrome_import.py passwords.csv
	create a private git repo for storage and push to it
	use pass commit to update changes, changes such as adding and removal of passwords auto commit and just need to be 
	pushed with pass commit
	you can make your passwords inaccessible to others using your computer without root access by using sudo chmod 000 pass
	when not in use then sudo chmod 777 pass so that you have a master key to your passwords

	Enjoy!
