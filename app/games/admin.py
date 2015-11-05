from django.contrib import admin
from .models import Game


class GamePuzzleInline(admin.StackedInline):
    extra = 0
    model = Game.puzzles.through
    verbose_name = "puzzle"
    verbose_name_plural = "puzzles in this game"

    def has_delete_permission(self, request, obj=None):
        if obj:
            return False

    def get_readonly_fields(self, request, obj=None):
        result = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        result.remove('id')
        if obj:
            return result
        else:
            return []

    def get_max_num(self, request, obj=None):
        if obj:
            return obj.puzzles.count()
        else:
            return super(GamePuzzleInline, self).get_max_num(request)


class GameAdmin(admin.ModelAdmin):
    exclude = ('puzzles', )
    inlines = [
        GamePuzzleInline,
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['delay', 'puzzles']
        return []

admin.site.register(Game, GameAdmin)
