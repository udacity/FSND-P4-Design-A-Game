- **App Architecture**
    - Meets Specification: App is architected as a Web Service API.
    - Meets Specification: App supports a variety of possible front-end clients.

- **New game implemented**
    - Meets Specification: A new type of game is implemented with additional
    game logic or features (such as 2-player games). New models may be required.
    - Meets Specification: "Illegal" moves are handled gracefully by the API. For
    example, if implementing Tic-Tac-Toe, if a User tries to play a square that 
    has already been filled - the server will respond with an error message
    explaining that the move is illegal. There should be no 'Internal Server
    Errors' so long as User input is otherwise properly formed.
    
- **New game documented**
    - Meets Specification: The new game is documented in a README.md file, with
    explanation of the rules and score-keeping so that it is possible to
    understand how to use the API without reading the source code.
    
- **New endpoints created**
    - Meets Specification: required endpoints are implemented with behavior that
    follows the project description.
    - Meets Specification: `get_game_history` is created. The output should be
    sufficient to 'replay' the game from start to finish and get the same result
    (notwithstanding any randomization inherent to the game).
    
- **New endpoints use correct http methods**
    - Meets Specification: Additional endpoints make use of sensible http methods.
    
- **Resource Containers**
    - Meets Specification: All endpoints make use of sensible Resource Containers.

- **New endpoints are documented**
    - Meets Specification: Additional endpoints behavior is explained, and
    parameters and return variables detailed.

- **Code Readability**
    - Meets Specification: Code formatting follows consistent rules for variable,
    function, class etc. naming conventions. Line length is not excessive and
    white-space is used appropriately to improve readability.
    - Meets Specification: Functions and methods include descriptive docstrings,
    and code that is not intuitively understandable includes comments.
     
- **Documentation**
    - Meets Specification: A README file is included with steps necessary to run
    the application locally.
    
- **Task Queues**
    - Meets Specification: The email reminder cronjob handler is modified so 
    that only Users 'needing' a reminder (actual logic up to the student) is
    modified.
    