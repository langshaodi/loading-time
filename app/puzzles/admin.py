from django.contrib import admin
from .models import *


class PuzzleAnswerOptionInline(admin.StackedInline):
    extra = 1
    model = PuzzleAnswerOption


class PuzzleAdmin(admin.ModelAdmin):
    inlines = [
        PuzzleAnswerOptionInline,
    ]

admin.site.register(Puzzle, PuzzleAdmin)
