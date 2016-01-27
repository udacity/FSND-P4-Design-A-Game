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
 a Number) such as Hangman, or a simple board game like Tic-Tac-Toe. Make
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

Define what a "score" for each game will be (beyond just won/lost for single
player games) and keep this data in your database.
For example in 'Guess a Number' the Score model stores the number of guesses
taken before the number was found. Lower guesses would be better - this
scoring system could also be extended to take into account how wide the original
range of numbers was as well! 

Note: if you're creating a two-player game you might want to
just record *who* won each game, although you could store additional data if
you like.

Be sure to document your game. Your README file should include instructions for
playing the game, and detailed descriptions of each endpoint (remember, you 
are documenting an API that another programmer may want to use as the basis for
a web or mobile app). An api user should *not* need to read the source code
to understand how to use it. You may follow the format of 'Guess a Number'.

###Task 3:
 Document your design decisions by answering the following questions:
   
- What additional fields did you add to your models and why?
- What were some of the trade-offs or struggles you faced when implementing
the new game logic?
       
###Task 4:
We'd like you to get additional practice working with the Datastore and 
performing queries and filters so we ask that you implement several additional 
endpoints. You'll want to customize them somewhat to fit the type of 
game you implement. Ensure that each endpoint uses the correct HTTP Method.
Finally, these endpoints should be documented in your README just like the ones
for Guess a Number.

 - **get_user_games**
    - Sometimes the urlsafe Key strings for games could be lost or garbled by client
    software. Create an endpoint that returns all of a User's active games.
    - You may want to modify the `User` and `Game` models to simplify this type
    of query. Hint: it might make sense for each game to be a `descendant` of a `User`.
    
 - **cancel_game**
    - Occasionally a User want to cancel a game they are playing. Create an endpoint
     that allows user to cancel a game. You could implement this by deleting the
     Game model itself, or add a Boolean field such as 'cancelled' to the model.
     Ensure that Users are not permitted to remove *completed* games - we don't
     want them manipulating their high score history!
    
 - **get_high_scores**
    - Remember how you defined a score in Task 2? Now we will use that to generate
     a list of high scores in descending order - a leader-board!
    - Accept an optional parameter `number_of_results` that limits the number of 
    results returned.
    - Note: If you choose to implement a 2-player game this endpoint is not required.
    
 - **get_user_rankings**
    - Come up with a method for ranking the performance of each player. For
    "Guess a Number" this could be by winning percentage with ties broken by the 
    average number of guesses.
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
In the skeleton Guess a Number project, a cron job and associated handler 
have been created (see cron.yaml and main.py). This sends an hourly reminder email to 
every User with an email address to try out 'Guess a Number'. Obviously, this is
probably annoying the Users.

Modify the SendReminderEmail handler so that this reminder email is only sent to
users that have incomplete games (or some other logic that makes sense to you).
Make sure to update the message to reflect this.
If you're feeling really ambitious you could try to implement even more complicated
logic or functionality. For example: "If the User has not made a move in an 
active game for more than 12 hours, send a reminder email that includes the 
current game state." 

###Task 6 (optional):
If you created a two-player game in Task 2, you might want to try implementing
a notification system!
When one user makes a move, add a task to the task queue to notify the User's
opponent that it's their turn. You can use the `SendReminderEmail` handler in
main.py as a template. However, remember that you will need to pass parameters
to identify the game and User that should receive the reminder. Don't forget
to update `app.yaml` with the new Handler listing. Finally, consult Google
App Engine documentation for [Using Push Queues in Python](https://cloud.google.com/appengine/docs/python/taskqueue/overview-push).
