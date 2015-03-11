-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database
CREATE DATABASE tournament;

--CREATE TABLES --

-- Create player table
CREATE TABLE players (id serial primary key, name text)
-- Create matches table which contains the data from the matches.
    -- THe id references the ID in players so we can't have any other player.
    -- The result is a real so should represent 1 to winner and 0 to loser.
CREATE TABLE matches (id INTEGER REFERENCES players, result REAL)

-- standings view
-- Contains the players and their win records, sorted by wins.
CREATE VIEW standings AS
    SELECT players.id, players.name, COALESCE(sum(matches.result), 0) AS wins, count(matches.result)
    FROM players LEFT JOIN matches
    ON players.id = matches.id
    GROUP BY players.id
    ORDER BY wins DESC;