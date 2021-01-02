from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """ ListAdmin Model Definition """

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("^name",)

    filter_horizontal = ("rooms",)