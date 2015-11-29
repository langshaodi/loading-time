from django.core.management.base import BaseCommand
from puzzles.models import Puzzle, PuzzleAnswerOption
import os


def get_or_create(model, **kwargs):
    try:
        m = model.objects.get(**kwargs), 0
        return m
    except model.DoesNotExist:
        return model.objects.create(**kwargs), 1


class Command(BaseCommand):
    help = 'Builds the question database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--print', dest='print', action='store_true',
            help='Print out all questions verbosely.'
        )

    def handle(self, *args, **options):
        print "Building questions from data file."
        f = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), '..', 'data/questions.txt')
        f = open(f, 'r')
        lines = f.read().split("\n")

        to_obj = []

        for l in lines:
            try:
                question, answer = l.split("ANS")
                a, b, x, y = [r.strip().lower() if r.strip(
                ) != "_" else None for r in
                    question.replace(' is to ', '-').replace(
                    ' as ', '-').split("-")]
                answers = [(ans.strip().lower(), True) if ans.strip(
                )[0].isupper() else (
                    ans.strip(), False) for ans in
                    answer.strip().split(",")]
            except Exception as e:
                print e
                raise Exception("Invalid format: {}".format(l))
            if True not in [r[1] for r in answers]:
                raise Exception("No correct answer indicated: {}".format(l))
            to_obj.append((a, b, x, y, answers))

        for obj in to_obj:
            a, b, x, y, answers = obj
            puzzle, c = get_or_create(
                Puzzle,
                comparison_a_1=a,
                comparison_a_2=b,
                comparison_b_1=x,
                comparison_b_2=y
            )
            for a in answers:
                ans = get_or_create(
                    PuzzleAnswerOption,
                    puzzle=puzzle,
                    text=a[0],
                    correct=a[1]
                )
            if options['print']:
                print ("Question:       {}\n" +
                       "Answers:        {}\n" +
                       "Correct answer: {}\n").format(
                    puzzle.question(),
                    [str(pa.text)
                     for pa in puzzle.puzzleansweroption_set.all()],
                    puzzle.correct_answer().text
                )
