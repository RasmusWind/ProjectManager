from django.contrib import admin
from .models import Task, Todo
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    model = Task

admin.site.register(Task, TaskAdmin)


class TodoAdmin(admin.ModelAdmin):
    model = Todo

admin.site.register(Todo, TodoAdmin)