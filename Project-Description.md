#Project Motivation and Overview
In the 'Developing Scalable Apps with Python' course you learned how to write
platform-agnostic apps using Google App Engine backed by Google Datastore.
 
 In this project you will be developing your own game! It won't have an interface,
 but will instead expose several API endpoints that will allow anyone to develop
 a front-end application to "play" your game.
 
 You won't be required to develop a front-end, all the added functionality will
 be testable with API Explorer. Let's get started!
 
###Task 1:
  Get the skeleton 'Guess a Number' application up and running. Read through the
 code and documentation, and test the endpoints. Make sure you understand 
 how different entities are created, how they fit together, and the overall flow.
 Create a User or two and play a few games. Make sure to take a look at the admin
 Datastore viewer (usually localhost:8000) to check out the various entities.
 
###Task 2:
  Come up with a new game to implement! This could be a guessing game (like Guess
 a Number) such as Hangman, or something more complex like Tic-Tac-Toe. Make
 sure that the existing endpoints work with the new game - you'll need to modify
 the models, forms, and resource containers, but the general structure should stay
 roughly the same so that Games can be created, moves played, and the game state
 updated and stored according to the rules.
 
 Some ideas you may want to consider:
    - Hangman, Tic-Tac-Toe, Battleship, mancala, yahtzee, solitaire.
    - 2 player games. For example, Tic-Tac-Toe could be implemented as a 
    single player game (in which case you'll want to write an AI for the User
    to play against). Or, you could allow for two players to play against 
    each other.  In the case of Tic-Tac-Toe this would make the endpoints and 
    data structure somewhat more complicated, but it would simplify the coding 
    because an "AI" would not be required.
    
Be sure to document your game. Your README file should include instructions for
playing the game, and detailed descriptions of each endpoint (remember, you 
are documenting an API that another programmer may want to use as the basis for
a web or mobile app). You may follow the format of 'Guess a Number'.

###Task 3:
 Document your design decisions by answering the following questions:
    - What additional fields did you add to your models and why?
    - What were some of the trade-offs or struggles you faced when implementing
      the new game logic?
       
###Task 4:
Implement additional endpoints. We'd like you to get additional practice working
with the Datastore and performing queries and filters so we ask that you implement
these additional endpoints. You'll want to customize them somewhat to fit the
type of game you implement.

Make sure that the endpoints are documented in your README just like the ones
for Guess a Number.

 - **get_user_games**
    - Sometimes the urlsafe Key strings for games could be lost or garbled by client
    software. Create an endpoint that returns all of a User's current games.
    - You may want to modify the `User` and `Game` models. Hint: it might make
    sense for each game to be a `descendant` of a `User`.
    
 - **get_high_scores**
    - Right now the **get_scores** endpoint returns all scores. Create a new endpoint
    that returns only 'winning' scores, with better scores coming first. Accept
    and optional parameter `number_of_results` that limits the number of results
    returned.
    
 - **get_user_ranking**
    - Come up with a method for ranking the performance of each player. For
    "Guess a Number" this could be the ratio of won/lost games (watch out for 
    division by zero!) with ties broken by the average number of guesses.
    - Create an endpoint that returns this player ranking. The results should 
    include each Player's name and the 'performance' indicator (eg. win/loss
    ratio).
 
 - **get_game_history**
    - Your API Users may want to be able to see a 'history' of moves for each game.
    - For example, Chess uses a format called 
    [PGN](https://en.wikipedia.org/wiki/Portable_Game_Notation) which allows
    any game to be replayed and watched move by move.
    - Add the capability for a Game's history to be presented in a similar way.
    For example: If a User made played 'Guess a Number' with the moves:
    (5, 8, 7), and received messages such as: ('Too low!', 'Too high!',
    'You win!'), an endpoint exposing the game_history might produce something like:
    [('Guess': 5, result: 'Too low'), ('Guess': 8, result: 'Too high'),
    ('Guess': 7, result: 'Win. Game over')].
    - Adding this functionality will require some additional properties in the
    'Game' model along with a Form, and endpoint to present the data to the User.

###Task 5:
Implement an additional endpoint of your choice?