from django.contrib import admin
from .models import *


class PuzzleAnswerOptionInline(admin.StackedInline):
    min_num = 4
    max_num = 4

    model = PuzzleAnswerOption


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('question_with_answer',)
    inlines = [
        PuzzleAnswerOptionInline,
    ]

admin.site.register(Puzzle, PuzzleAdmin)
