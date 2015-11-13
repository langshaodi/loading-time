from rest_framework import serializers
from .models import Puzzle, PuzzleAnswerOption


class PuzzleAnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PuzzleAnswerOption


class PuzzleSerializer(serializers.ModelSerializer):
    answers = PuzzleAnswerOptionSerializer(
        many=True, source='puzzleansweroption_set')

    class Meta:
        model = Puzzle
        fields = ('id', 'question', 'answers')
