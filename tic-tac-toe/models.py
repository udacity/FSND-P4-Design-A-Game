import random
from datetime import date
from protorpc import messages
from google.appengine.ext import ndb


class User(ndb.Model):
    """User profile"""
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    wins = ndb.IntegerProperty(default=0)
    total_played = ndb.IntegerProperty(default=0)

    @property
    def win_percentage(self):
        if self.total_played > 0:
            return float(self.wins)/float(self.total_played)
        else:
            return 0

    def to_form(self):
        return UserForm(name=self.name,
                        email=self.email,
                        wins=self.wins,
                        total_played=self.total_played,
                        win_percentage=self.win_percentage)

    def add_win(self):
        """Add a win"""
        self.wins += 1
        self.total_played += 1
        self.put()

    def add_loss(self):
        """Add a loss"""
        self.total_played += 1
        self.put()


class Game(ndb.Model):
    """Game object"""
    board = ndb.PickleProperty(required=True)
    next_move = ndb.KeyProperty(required=True) # The User's whose turn it is
    user_x = ndb.KeyProperty(required=True, kind='User')
    user_o = ndb.KeyProperty(required=True, kind='User')
    game_over = ndb.BooleanProperty(required=True, default=False)
    winner = ndb.KeyProperty()
    history = ndb.PickleProperty(required=True)

    @classmethod
    def new_game(cls, user_x, user_o):
        """Creates and returns a new game"""
        game = Game(user_x=user_x,
                    user_o=user_o,
                    next_move=user_x)
        game.board = ['' for _ in range(9)]
        game.history = []
        game.put()
        return game

    def to_form(self):
        """Returns a GameForm representation of the Game"""
        form = GameForm(urlsafe_key=self.key.urlsafe(),
                        board = str(self.board),
                        user_x=self.user_x.get().name,
                        user_o=self.user_o.get().name,
                        next_move=self.next_move.get().name,
                        game_over=self.game_over)
        if self.winner:
            form.winner = self.winner.get().name
        return form

    def end_game(self, winner):
        """Ends the game"""
        self.winner = winner
        self.game_over = True
        self.put()
        loser = self.user_o if winner == self.user_x else self.user_x
        # Add the game to the score 'board'
        score = Score(date=date.today(), winner=winner, loser=loser)
        score.put()

        # Update the user models
        winner.get().add_win()
        loser.get().add_loss()


class Score(ndb.Model):
    """Score object"""
    date = ndb.DateProperty(required=True)
    winner = ndb.KeyProperty(required=True)
    loser = ndb.KeyProperty(required=True)

    def to_form(self):
        return ScoreForm(date=str(self.date),
                         winner=self.winner.get().name,
                         loser=self.loser.get().name)


class GameForm(messages.Message):
    """GameForm for outbound game state information"""
    urlsafe_key = messages.StringField(1, required=True)
    board = messages.StringField(2, required=True)
    user_x = messages.StringField(3, required=True)
    user_o = messages.StringField(4, required=True)
    next_move = messages.StringField(5, required=True)
    game_over = messages.BooleanField(6, required=True)
    winner = messages.StringField(7)


class GameForms(messages.Message):
    """Container for multiple GameForm"""
    items = messages.MessageField(GameForm, 1, repeated=True)

class NewGameForm(messages.Message):
    """Used to create a new game"""
    user_x = messages.StringField(1, required=True)
    user_o = messages.StringField(2, required=True)


class MakeMoveForm(messages.Message):
    """Used to make a move in an existing game"""
    user_name = messages.StringField(1, required=True)
    move = messages.IntegerField(2, required=True)


class ScoreForm(messages.Message):
    """ScoreForm for outbound Score information"""
    date = messages.StringField(1, required=True)
    winner = messages.StringField(2, required=True)
    loser = messages.StringField(3, required=True)


class ScoreForms(messages.Message):
    """Return multiple ScoreForms"""
    items = messages.MessageField(ScoreForm, 1, repeated=True)


class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    message = messages.StringField(1, required=True)


class UserForm(messages.Message):
    """User Form"""
    name = messages.StringField(1, required=True)
    email = messages.StringField(2)
    wins = messages.IntegerField(3, required=True)
    total_played = messages.IntegerField(4, required=True)
    win_percentage = messages.FloatField(5, required=True)


class UserForms(messages.Message):
    """Container for multiple User Forms"""
    items = messages.MessageField(UserForm, 1, repeated=True)

