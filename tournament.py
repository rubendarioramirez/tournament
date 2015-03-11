#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    #execute the query
    c.execute("DELETE FROM matches")
    #commit delete if all goes fine
    db.commit()
    #close the database since i dont need it anymore
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    #execute the query
    c.execute("DELETE FROM players")
    #commit delete if all goes fine
    db.commit()
    #close the database since i dont need it anymore
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    #execute the query
    c.execute("SELECT COUNT(name) FROM players")
    #store the results in a variable named result
    results = c.fetchone()[0]
    #close the database since i dont need it anymore
    db.close()

    return results
    
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    #execute the query - The %s means save this space for the variable, and then i definy the variable outside
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    #commit if all goes fine
    db.commit()
    #close the database since i dont need it anymore
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    #execute the query - The %s means save this space for the variable, and then i definy the variable outside
    c.execute("SELECT * FROM standings")

    return c.fetchall()
    #close the database since i dont need it anymore
    db.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #Connect to database
    db = connect()
    #create the cursor
    c = db.cursor()
    
    #execute the query for the winner
    c.execute("INSERT INTO matches (id, result) VALUES (%s, 1)", (winner,))
    #commit if all goes fine
    db.commit()

    #execute the query for the loser
    c.execute("INSERT INTO matches (id, result) VALUES (%s, 0)", (loser,))
    #commit if all goes fine
    db.commit()

    #close the database since i dont need it anymore
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    return [(standings[i-1][0], standings[i-1][1], standings[i][0], standings[i][1])
            for i in range(1, len(standings), 2)]

