from django.contrib import admin

from django101.tasks.models import Task


# Variant 1
# admin.site.register(Task)

# Variant 2
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    sortable_by = ('title',)
