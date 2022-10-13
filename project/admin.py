from django.contrib import admin
from .models import Task, Todo
# Register your models here.

class TodoInline(admin.TabularInline):
    model = Todo

class TaskAdmin(admin.ModelAdmin):
    model = Task
    inlines = [TodoInline]

admin.site.register(Task, TaskAdmin)


class TodoAdmin(admin.ModelAdmin):
    model = Todo

admin.site.register(Todo, TodoAdmin)