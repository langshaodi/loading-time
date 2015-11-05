from rest_framework import serializers
from .models import Game
from puzzles.serializers import PuzzleSerializer


class GameSerializer(serializers.ModelSerializer):
    puzzles = PuzzleSerializer(many=True, read_only=True)

    class Meta:
        model = Game
