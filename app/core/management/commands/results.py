from django.core.management.base import BaseCommand
from puzzles.models import *
from games.models import *
from responses.models import *


class Command(BaseCommand):
    help = 'Builds the question database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--print', dest='print', action='store_true',
            help='Print out all questions verbosely.'
        )

    def handle(self, *args, **options):
        for response in Response.objects.all():
            # Non-control games
            for game in GameResponse.objects.filter(
                    response=response, game__default=False):
                print
                print "Game with delay:  {}".format(game.game.delay)
                print "User Frustration: {}/5".format(game.frustration)
                num_correct = 0
                total_time = 0
                puzzles = PuzzleResponse.objects.filter(game_response=game)
                for puzzle in puzzles:
                    if puzzle.answer == puzzle.puzzle.correct_answer():
                        num_correct += 1
                    total_time += puzzle.time / 1000
                ratio_correct = float(num_correct) / len(puzzles)
                average_time  = float(total_time) / len(puzzles)
                print "% correct:        {}".format(ratio_correct)
                print "Average time:     {}".format(average_time)
