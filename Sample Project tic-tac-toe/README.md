#Full Stack Nanodegree Project 4 Refresh

## Set-Up Instructions:
1.  Update the value of application in app.yaml to the app ID you have registered
 in the App Engine admin console and would like to use to host your instance of this sample.
1.  Run the app with the devserver using dev_appserver.py DIR, and ensure it's
 running by visiting your local server's address (by default localhost:8080.)
1.  (Optional) Generate your client library(ies) with the endpoints tool.
 Deploy your application.
 
 
##Game Description:
Tic-Tac-Toe is a simple two player game. Game instructions are available
[here](https://en.wikipedia.org/wiki/Tic-tac-toe).

The board is represented as a 1-D list of squares with indexes as follows:
[0, 1, 2
 3, 4, 5
 6, 7, 8]
 

##Files Included:
 - api.py: Contains endpoints and game playing logic.
 - app.yaml: App configuration.
 - cron.yaml: Cronjob configuration.
 - main.py: Handler for taskqueue handler.
 - models.py: Entity and message definitions including helper methods.
 - utils.py: Helper function for retrieving ndb.Models by urlsafe Key string.

##Endpoints Included:
 - **create_user**
    - Path: 'user'
    - Method: POST
    - Parameters: user_name
    - Returns: Message confirming creation of the User.
    - Description: Creates a new User. user_name provided must be unique. Will 
    raise a ConflictException if a User with that user_name already exists.
    
 - **new_game**
    - Path: 'game'
    - Method: POST
    - Parameters: user_x, user_y
    - Returns: GameForm with initial game state.
    - Description: Creates a new Game. `user_x` and `user_o` are the names of the
    'X' and 'O' player respectively
     
 - **get_game**
    - Path: 'game/{urlsafe_game_key}'
    - Method: GET
    - Parameters: urlsafe_game_key
    - Returns: GameForm with current game state.
    - Description: Returns the current state of a game.
    
 - **make_move**
    - Path: 'game/{urlsafe_game_key}'
    - Method: PUT
    - Parameters: urlsafe_game_key, user_name, move
    - Returns: GameForm with new game state.
    - Description: Accepts a move and returns the updated state of the game.
    A move is a number from 0 - 8 corresponding to one of the 9 possible
    positions on the board.
    If this causes a game to end, a corresponding Score entity will be created,
    unless the game is tied - in which case the game will be deleted.
    
 - **get_scores**
    - Path: 'scores'
    - Method: GET
    - Parameters: None
    - Returns: ScoreForms.
    - Description: Returns all Scores in the database (unordered).
    
 - **get_user_scores**
    - Path: 'scores/user/{user_name}'
    - Method: GET
    - Parameters: user_name
    - Returns: ScoreForms. 
    - Description: Returns all Scores recorded by the provided player (unordered).
    Will raise a NotFoundException if the User does not exist.
    
 - **get_active_game_count**
    NOT IMPLEMENTED
    - Path: 'games/active'
    - Method: GET
    - Parameters: None
    - Returns: StringMessage
    - Description: Gets the average number of attempts remaining for all games
    from a previously cached memcache key.

##Models Included:
 - **User**
    - Stores unique user_name and (optional) email address.
    - Also keeps track of wins and total_played.
    
 - **Game**
    - Stores unique game states. Associated with User models via KeyProperties
    user_x and user_o.
    
 - **Score**
    - Records completed games. Associated with Users model via KeyProperty as
    well.
    
##Forms Included:
 - **GameForm**
    - Representation of a Game's state (urlsafe_key, board,
    user_x, user_o, game_over, winner).
 - **NewGameForm**
    - Used to create a new game (user_x, user_o)
 - **MakeMoveForm**
    - Inbound make move form (user_name, move).
 - **ScoreForm**
    - Representation of a completed game's Score (date, winner, loser).
 - **ScoreForms**
    - Multiple ScoreForm container.
 - **UserForm**
    - Representation of User. Includes winning percentage
 - **UserForms**
    - Container for one or more UserForm.
 - **StringMessage**
    - General purpose String container.
    
    
##Design Decisions
- I added a field to store the board in Game. I used PickleProperty because it allowed
me to store a Python List in the datastore which seemed like the simplest way
to record the state of the board.
- I also added next_move, user_x, user_o, and winner (all KeyProperty) to the Game
model to keep track of which User was either 'X' or 'O' and who's move it was.
- I used a 'game_over' flag as well to mark completed games.
- I modified the Score model to record which player won and lost each game.

The 1-d list to represent the board was the simplest solution I could think of, 
but it would make it very hard to scale the game to 4x4 or nxn versions of 
tic-tac-toe because there's no way to automatically partition each row with a 
1-d array. Also the winner checking logic is very hard-coded. 
I don't feel great about the logic to track which player's turn it is, 
but everything seems to work.

##Additional endpoints
 - **get_user_games**
    - Path: 'user/games'
    - Method: GET
    - Parameters: user_name
    - Returns: GameForms with 1 or more GameForm inside.
    - Description: Returns the current state of all the User's active games.
    
 - **cancel_game**
    - Path: 'game/{urlsafe_game_key}'
    - Method: DELETE
    - Parameters: urlsafe_game_key
    - Returns: StringMessage confirming deletion
    - Description: Deletes the game. If the game is already completed an error
    will be thrown.
    
 - **get_user_rankings**
    - Path: 'user/ranking'
    - Method: GET
    - Parameters: None
    - Returns: UserForms
    - Description: Rank all players that have played at least one game by their
    winning percentage and return.

 - **get_game_history**
    - Path: 'game/{urlsafe_game_key}'
    - Method: GET
    - Parameters: urlsafe_game_key
    - Returns: StringMessage containing history
    - Description: Returns the move history of a game as a stringified list of 
    tuples in the form (square, symbol) eg: [(0, 'X'), (4, 'O')]