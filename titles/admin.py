from django.contrib import admin

from titles.models import Title, Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'rating')
    search_fields = ("text",)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = '-пусто-'


admin.site.register(Genre, GenreAdmin)

