from django.db import models
from django.conf import settings
import random


def random_timeout():
    return random.randint(
        settings.DELAY_LOWER_BOUND, settings.DELAY_UPPER_BOUND)


class Game(models.Model):
    puzzles = models.ManyToManyField(
        'puzzles.Puzzle')
    delay = models.BigIntegerField(
        default=random_timeout, blank=False, null=False)

    default = models.BooleanField(default=False)

    def num_puzzles(self):
        return len(self.puzzles.all())

    def __repr__(self):
        return "Game with " + str(self.num_puzzles()) + \
            " puzzle(s) and delay: " + str(self.delay)

    def __str__(self):
        return self.__repr__()

    def save(self, *args, **kwargs):
        if self.default:
            try:
                temp = Game.objects.get(
                    default=True)
                if self != temp:
                    temp.default = False
                    temp.save()
            except Game.DoesNotExist:
                pass
        super(Game, self).save(*args, **kwargs)
