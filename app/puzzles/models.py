from django.db import models


class Puzzle(models.Model):
    text = models.CharField(max_length=1000, blank=False, null=False)

    def correct_answer(self):
        try:
            return PuzzleAnswerOption.objects.get(correct=True, puzzle=self)
        except PuzzleAnswerOption.DoesNotExist:
            return None

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()


class PuzzleAnswerOption(models.Model):
    puzzle = models.ForeignKey(Puzzle)
    correct = models.BooleanField(blank=False, null=False, default=False)
    text = models.CharField(max_length=500, blank=True, null=True)
    image = models.FileField(upload_to='media/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.correct:
            try:
                temp = PuzzleAnswerOption.objects.get(
                    correct=True, puzzle=self.puzzle)
                if self != temp:
                    temp.correct = False
                    temp.save()
            except PuzzleAnswerOption.DoesNotExist:
                pass
        super(PuzzleAnswerOption, self).save(*args, **kwargs)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()
