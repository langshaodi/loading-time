from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Game
from .serializers import *
from puzzles.models import Puzzle
from django.conf import settings


class GameView(APIView):
    """
    A viewset for viewing and editing games
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        puzzles = Puzzle.objects.all().order_by(
            '?')[:settings.NUM_OF_PUZZLES]

        game = Game.objects.create()
        game.puzzles = puzzles
        game.save()

        return Response(
            GameSerializer(game).data
        )
