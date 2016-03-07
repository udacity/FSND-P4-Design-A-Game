### Task 1:

- **API Architecture**
    - App is architected as a Web Service API.
    - App supports a variety of possible front-end clients.

### Task 2:

- **API Implementation**
    - A new type of game is implemented with additional game logic or features (such as 2-player games).
      The new game is not a copy of Guess a Number.
      If it is a guessing game like Hangman, additional features are included (partial reveal of the solution over time).
    - "Illegal" moves are handled gracefully by the API.
      For example, if implementing Tic-Tac-Toe, if a User tries to play a square that has already been filled - the server will respond with an error message explaining that the move is illegal.
      There should be no 'Internal Server Errors' so long as User input is otherwise properly formed.

- **Resource Containers**
    - All endpoints make use of sensible Resource Containers.

### Task 3:

- **New Endpoints Created**
    - Required endpoints are implemented with behavior that follows the project description.
    
- **Appropriate use of HTTP Methods**
    - Additional endpoints make use of appropriate HTTP methods.

### Task 4:

- **Task Queues**
    - The email reminder cronjob handler is modified so that only Users 'needing' a reminder (actual logic up to the student) is modified.
    
### Task 5:

- **Code Quality**
    - Code is ready for personal review and neatly formatted.

- **Code Readability**
    - Code formatting follows consistent rules for variable, function, class etc. naming conventions. Line length is not excessive and white-space is used appropriately to improve readability.
    - Functions and methods include descriptive docstrings, and code that is not immediately understandable includes comments.

- **Documentation**
    - A README file is included with steps necessary to run the application locally.
    - The new game is documented in a README.md file, with explanation of the rules and score-keeping.
    - The API is documented so that users can understand how to use the API without reading the source code.
    - The student has meaningfully reflected on their design decisions and recorded their reflections in README.md.
