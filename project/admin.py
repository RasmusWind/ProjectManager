from django.contrib import admin
from .models import Task, Todo, Worker, Team
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

class WorkerAdmin(admin.ModelAdmin):
    model = Worker

admin.site.register(Worker, WorkerAdmin)

class TaskInline(admin.TabularInline):
    model = Task

class TeamAdmin(admin.ModelAdmin):
    model = Team
    filter_horizontal = ("workers",)
    inlines = [TaskInline]

admin.site.register(Team, TeamAdmin)