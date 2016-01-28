import logging
from google.appengine.ext import ndb
import endpoints

def get_by_urlsafe(urlsafe, model):
    """Returns an ndb.Model entity that the urlsafe key points to. Checks
        that the type of entity returned is of the correct kind. Raises an
        error if the key String is malformed or the entity is of the incorrect
        kind
    Args:
        urlsafe: A urlsafe key string
        model: The expected entity kind
    Returns:
        The entity that the urlsafe Key string points to or None if no entity
        exists.
    Raises:
        ValueError:"""
    try:
        key = ndb.Key(urlsafe=urlsafe)
    except TypeError:
        raise endpoints.BadRequestException('Invalid Key')
    except Exception, e:
        if e.__class__.__name__ == 'ProtocolBufferDecodeError':
            raise endpoints.BadRequestException('Invalid Key')
        else:
            raise

    entity = key.get()
    if not entity:
        return None
    if not isinstance(entity, model):
        raise ValueError('Incorrect Kind')
    return entity


def check_winner(board):
    """Check the board. If there is a winner, return the symbol of the winner"""
    # Check rows
    for i in range(3):
        if board[3*i]:
            if board[3*i] == board[3*i + 1] and board[3*i] == board[3*i + 2]:
                return board[3*i]
    # Check columns
    for i in range(3):
        if board[i]:
            if board[i] == board[i + 3] and board[i] == board[i + 6]:
                return board[i]
    # Check diagonals
    if board[0]:
        if board[0] == board[4] and board[0] == board[8]:
            return board[0]
    if board[2]:
        if board[2] == board[4] and board[2] == board[6]:
            return board[2]

def check_full(board):
    """Return true if the board is full"""
    for cell in board:
        if not cell:
            return False
    return True