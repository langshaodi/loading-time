from rest_framework.views import APIView
from rest_framework.response import Response as DRFResponse
from .models import *
from .serializers import *
from games.models import Game
from puzzles.models import Puzzle, PuzzleAnswerOption
from rest_framework.exceptions import ParseError
from django.db import transaction
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
import sys, os


class UnsafeSessionAuthentication(SessionAuthentication):

    def authenticate(self, request):
        http_request = request._request
        user = getattr(http_request, 'user', None)

        if not user or not user.is_active:
            return None

        return (user, None)


class ResponseView(APIView):
    """
    A viewset to submit responses. POST to submit a response.
    """
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (
        UnsafeSessionAuthentication, )

    def post(self, request, format=None):
        games = []
        answers = []
        user = Response.objects.create()
        with transaction.atomic():
            try:
                for g in request.data.get('games', []):
                    game_obj = Game.objects.get(
                        pk=g['responses'][0]['game_id'])
                    r_obj = GameResponse.objects.create(
                        game = game_obj,
                        response = user,
                        frustration=g.get('frustration'),
                    )
                    games.append(game_obj)
                    for resp in g['responses']:
                        puzzle_obj = Puzzle.objects.get(
                            pk=resp['puzzle_id']
                        )
                        answer_obj = PuzzleAnswerOption.objects.get(
                            pk=resp['answer_id']
                        )
                        p_obj = PuzzleResponse.objects.create(
                            game_response=r_obj,
                            puzzle=puzzle_obj,
                            answer=answer_obj,
                            time=resp['response_time_in_ms']
                        )
                        answers.append(answer_obj)
            except Exception as e:
                print e
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                raise ParseError(
                    "The server did not understand the request.")

        if games == [] or answers == []:
            raise ParseError("No response data found in request.")
        else:
            return DRFResponse("y'all did a good thang")
