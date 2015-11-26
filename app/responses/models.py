from django.db import models


class Response(models.Model):
    submitted = models.DateTimeField(auto_now_add=True)


class GameResponse(models.Model):
    response = models.ForeignKey(Response)
    game = models.ForeignKey('games.Game')
    submitted = models.DateTimeField(auto_now_add=True)
    frustration = models.SmallIntegerField(blank=False, null=False)
    total_time = models.FloatField(blank=True, null=True)


class PuzzleResponse(models.Model):
    game_response = models.ForeignKey(GameResponse)
    puzzle = models.ForeignKey('puzzles.Puzzle')
    answer = models.ForeignKey('puzzles.PuzzleAnswerOption')
    time = models.FloatField()

    @property
    def correct(self):
        return self.puzzle.correct_answer() == self.answer
