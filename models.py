import random
from protorpc import messages
from google.appengine.ext import ndb

class Profile(ndb.Model):
    """User profile"""
    pass


class Game(ndb.Model):
    """Game object"""
    target = ndb.IntegerProperty(required=True)
    attempts_remaining = ndb.IntegerProperty(required=True, default=5)

    @classmethod
    def new_game(cls, min, max, attempts):
        """Creates and returns a new game"""
        print min, max, attempts
        if max < min:
            raise ValueError('Maximum must be greater than minimum')
        game = Game(target=random.choice(range(1, max + 1)),
                    attempts_remaining=attempts)
        game.put()
        return game

    def to_form(self, message):
        """Returns a GameForm representation of the Game"""
        form = GameForm()
        form.urlsafe_key = self.key.urlsafe()
        form.attempts_remaining = self.attempts_remaining
        form.message = message
        return form



class Score(ndb.Model):
    """Score object"""


class GameForm(messages.Message):
    """GameForm for outbound game state information"""
    urlsafe_key = messages.StringField(1, required=True)
    attempts_remaining = messages.IntegerField(2, required=True)
    message = messages.StringField(3, required=True)


class NewGameForm(messages.Message):
    """Used to create a new game"""
    min = messages.IntegerField(1, default=1)
    max = messages.IntegerField(2, default=10)
    attempts = messages.IntegerField(3, default=5)

class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    message = messages.StringField(1, required=True)

