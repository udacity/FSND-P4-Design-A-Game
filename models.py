from protorpc import messages
from google.appengine.ext import ndb

class Profile(ndb.Model):
    """User profile"""
    pass

class Game(ndb.Model):
    """Game object"""

class Score(ndb.Model):
    """Score object"""


class StringMessage(messages.Message):
    """StringMessage-- outbound (single) string message"""
    message = messages.StringField(1, required=True)

