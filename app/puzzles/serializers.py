from rest_framework import serializers
from .models import Puzzle, PuzzleAnswerOption


class PuzzleAnswerOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PuzzleAnswerOption


class PuzzleSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Puzzle

    def get_answers(self, obj):
        return PuzzleAnswerOptionSerializer(
            PuzzleAnswerOption.objects.filter(puzzle=obj),
            many=True).data
