from rest_framework import serializers
from .models import *
from games.serializers import GameSerializer
from puzzles.serializers import PuzzleSerializer


class ResponseSerializer(serializers.ModelSerializer):
    game = GameSerializer
    puzzles = PuzzleSerializer(many=True, read_only=True)
    game_responses = serializers.SerializerMethodField()

    class Meta:
        model = Response

    def get_game_responses(self):
        game_responses = []
        return game_responses


class GameResponseSerializer(serializers.ModelSerializer):
    puzzle_responses = serializers.SerializerMethodField()

    class Meta:
        model = GameResponse

    def get_puzzle_responses(self):
        return []


class PuzzleResponseSerializer(serializers.ModelSerializer):
    puzzle = PuzzleSerializer()

    class Meta:
        model = PuzzleResponse
