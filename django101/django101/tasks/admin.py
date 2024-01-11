from django.contrib import admin

from django101.tasks.models import Task


# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')
    list_filter = ('done',)
