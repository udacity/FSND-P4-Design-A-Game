import endpoints
from protorpc import remote, messages, message_types

from models import Game
from models import StringMessage, NewGameForm, GameForm
from utils import get_by_urlsafe

NEW_GAME_REQUEST = endpoints.ResourceContainer(NewGameForm)
GET_GAME_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    urlsafe_game_key=messages.StringField(1),
)

@endpoints.api(name='guess_a_number', version='v1')
class GuessANumberApi(remote.Service):
    """Game API"""

    @endpoints.method(response_message=StringMessage,
                      path='hello_world',
                      name='hello_world',
                      http_method='GET')
    def hello(self, request):
        return StringMessage(message='hello world')

    @endpoints.method(request_message=NEW_GAME_REQUEST,
                      response_message=GameForm,
                      path='game',
                      name='new_game',
                      http_method='POST')
    def new_game(self, request):
        """Creates new game"""
        game = Game.new_game(request.min, request.max, request.attempts)
        return game.to_form('Good luck playing Guess a Number!')

    @endpoints.method(request_message=GET_GAME_REQUEST,
                      response_message=GameForm,
                      path='game/{urlsafe_game_key}',
                      name='get_game',
                      http_method='GET')
    def get_game(self, request):
        """Return a current game state"""
        game = get_by_urlsafe(request.urlsafe_game_key, Game)

        if game:
            return game.to_form('Time to make a move!')
        else:
            raise endpoints.NotFoundException('Game not found!')


api = endpoints.api_server([GuessANumberApi])