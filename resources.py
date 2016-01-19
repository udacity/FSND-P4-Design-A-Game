import endpoints
from protorpc import remote

from models import StringMessage


@endpoints.api(name='guess_a_number', version='v1')
class GuessANumberApi(remote.Service):
    """Game API"""

    @endpoints.method(
            response_message=StringMessage,
            path='/hello_world',
            name='hello_world',
            http_method='GET'
    )
    def hello(self, request):
        return StringMessage(message='hello world')

api = endpoints.api_server([GuessANumberApi])