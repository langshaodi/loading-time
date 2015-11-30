from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Game
from .serializers import *
from puzzles.models import Puzzle
from django.conf import settings


class GameView(APIView):
    """
    A viewset to get new games. GET to generate a new game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        puzzles = [p for p in Puzzle.objects.all().order_by(
            '?') if p.correct_answer()][:settings.NUM_OF_PUZZLES]

        game = Game.objects.create()
        game.puzzles = puzzles
        game.save()

        return Response(
            GameSerializer(game).data
        )


class DefaultGameView(APIView):
    """
    A viewset to get the default game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        game = Game.objects.get(default=True)
        return Response(
            GameSerializer(game).data
        )


#/game/multi/?num=2..5
class MultiGameView(APIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny,)  


    def get(self, request, format=None):
        num = int(request.GET.get('num'))
        default_game = Game.objects.get(default=True)
    
        puzzles = [p for p in Puzzle.objects.all().order_by(
                '?') if p.correct_answer()]#[:settings.NUM_OF_PUZZLES]

        games = []
        for i in range(0,num):
            game = Game.objects.create()
            game.puzzles = puzzles[i*10:(i+1)*settings.NUM_OF_PUZZLES]
            game.save()
            games.append(GameSerializer(game).data)

        response = games
        return Response(
            response
        )