from django.contrib import admin

from blog.models import RequestForm


@admin.register(RequestForm)
class RequestFormAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'give_currency',
        'get_currency',
        'telegram',
    )
