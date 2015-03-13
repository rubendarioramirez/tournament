# tournament
Tournament project for UDACITY

Project Description: Tournament Planner
This project is a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: Database creation and Python functions to simulate the matches.

How to run this project:
-Install Vagrant and VirtualBox
-Clone the fullstack-nanodegree-vm repository
-Launch the Vagrant VM

Create the database:
Before you can run your code or create your tables, you'll need to use the create database command in psql to create the database. Use the name tournament for your database ==> "CREATE DATABASE tournament;"

Then you can connect psql to your new database and create your tables: This can be done in two ways.
-Paste each statement in to psql.
-Use the command \i tournament.sql to import the whole file into psql at once.

Test the functionality
In order to test if the project passes all the required test cases you should run tournament_test.py.
To do so type: python tournament_test.py in your terminal (Remember to be executing Vagrant and be inside the folder you have that file stored).
The results will be displayed in the terminal/command line
