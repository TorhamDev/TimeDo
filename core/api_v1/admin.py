from django.contrib import admin
from api_v1.models import Timer, ToDo
# Register your models here.


class TimerAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'start_time', 'end_time', 'is_archive']


admin.site.register(Timer, TimerAdmin)
admin.site.register(ToDo)