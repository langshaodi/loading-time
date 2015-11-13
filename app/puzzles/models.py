from django.db import models
from django.core.exceptions import ValidationError


class Puzzle(models.Model):
    comparison_a_1 = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="A", help_text="A:B::X:Y")
    comparison_a_2 = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="B", help_text="A:B::X:Y")
    comparison_b_1 = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="X", help_text="A:B::X:Y")
    comparison_b_2 = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="Y", help_text="A:B::X:Y")

    sep = "______"

    def correct_answer(self):
        try:
            return PuzzleAnswerOption.objects.get(correct=True, puzzle=self)
        except PuzzleAnswerOption.DoesNotExist:
            return None

    def clean(self):
        answers = [c for c in [self.comparison_a_1,
                               self.comparison_a_2,
                               self.comparison_b_1,
                               self.comparison_b_2] if c]
        if len(answers) > 3 or len(answers) < 3:
            raise ValidationError(
                "Exactly one part of the analogy must be blank.")

    def __repr__(self):
        return self.question()

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()

    def question(self):
        return "{} is to {} as {} is to {}. ({})".format(
            self.comparison_a_1.title() or self.sep,
            self.comparison_a_2 or self.sep,
            self.comparison_b_1 or self.sep,
            self.comparison_b_2 or self.sep,
            self.correct_answer() or "No Answer"
        )


class PuzzleAnswerOption(models.Model):
    puzzle = models.ForeignKey(Puzzle)
    correct = models.BooleanField(blank=False, null=False, default=False)
    text = models.CharField(max_length=500, blank=True, null=True)

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
