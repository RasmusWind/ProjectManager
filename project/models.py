from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    complete = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name="todos", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=200, blank=False)
    workers = models.ManyToManyField("Worker", related_name="workers")
    current_task = models.ForeignKey(Task, related_name="teams", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=200, blank=False)
    current_todo = models.ForeignKey(Todo, related_name="workers", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name