# Hangman with API

## About the project

I started this hangman game as a pet project for practicing python and to get a better understanding of how to get data out of an API. Also, I thought it would be cool if there could been statistics about the players, so I implemented a database and a shell script file which are responsible for the data handling.

*Note: The project was made for Linux environment!*

## Motivation

I had __three__ good reasons why I should implement this idea.

1. I wanted to practice python, API calls and SQL with shell script.
2. I needed at least one pet project for my school studies.
3. Back in the day, when we started learning python, we had a hangman project, but we did not really made it a greate project, so I thought: *Why not rewrite it and make it better?* 

## Technologies

* __Python__ as base programming language.
* __Bash script__ for connecting SQL to the program.
* __PostgreSQL__ for storing and handling data.
* __API__ for getting a random word.

## Features

* Thanks to API calls, there are no hard coded word list in the project.
* You only need a linux terminal to run the fully functioning program. (No need for IDE for SQL connection)
* Has statistics about players, who already played the game.

## Installation

If you do not have PostgreSQL installed, then please do! You are going to need it for the statistics. 

*Here is a helpful documentation how to do it: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04*

*Note: If you have an newer version, than ubuntu 18.04. __do not worry__ it is going to be the same process*

1. Clone the project first:
        1. Open up the terminal (Use __CTRL + ALT + T__ for that).
        2. Go to the repository where you want to have the projects directory.
        3. Clone the git repositry: *git clone https://github.com/havacs96/hangman-with-api.git*

2. Execute *create_database.sql* to create the database:
        1. Open up the terminal (Use __CTRL + ALT + T__ for that).
        2. Go into the *hangman-with-api* repository using the *cd* command.
        3. Execute the SQL file with this command: *psql -U username -d <myDataBase> -a -f create_database.sql* and replace <myDataBase> with your database's name.
	
3. Edit the data_handler.sh:
	* Done by terminal
		1. Go into the *hangman-with-api* repository using the *cd* command.
		2. Open the data_handler.sh using nano command (Write *nano data_handler.sh* to the reminal).
		3. Replace the environtmental variables for SQL by your postgerSQL settings.
		4. Save the changes!!!
	* Done by interface
		1. Go into the *hangman-with-api* repository.
		2. Open the data_handler.sh using your favourite text editor.
		3. Replace the environtmental variables for SQL by your postgerSQL settings.
		4. Save the changes!!!
	
## How to use the program

1. This is a terminal program, so open up a terminal window.
2. Go into the *hangman-with-api* repository using the *cd* command.
3. Run the *hangman.py*: Write in *python3 hangman.py*

The game will tell you everything else! __Enjoy!__

## Credits

Huge thanks for __Wordnik__ for granting API from where the program can get random words!

## Licence

MIT © Havacs Péter
