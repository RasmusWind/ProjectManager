from django.shortcuts import render
from .models import Task, Todo
from django.db import models
# Create your views here.

def seedTasks():
    # Opret en ny task via Model Manager'ens create metode. Denne gemmer automatisk til databasen.
    # Jeg gør derefter det samme for de tre todos, og sætter deres foreignkey til tasken.
    software_task = Task.objects.create(name="Produce software")
    
    software_todo1 = Todo.objects.create(title="Write code", task=software_task)
    software_todo2 = Todo.objects.create(title="Compile source", task=software_task)
    software_todo3 = Todo.objects.create(title="Test program", task=software_task)


    # Dette er en anden måde at lave instancer på.

    # Laver en Task instance som ikke er gemt i databasen.
    # coffee_task bliver først gemt i databasen når den kører save() metoden.
    coffee_task = Task()
    coffee_task.name = "Brew coffee"
    coffee_task.save()

    # Det samme gør jeg for todos
    coffee_todo1 = Todo()
    coffee_todo1.title = "Pour water"
    coffee_todo1.task = coffee_task
    coffee_todo2 = Todo()
    coffee_todo2.title = "Pour coffee"
    coffee_todo2.task = coffee_task
    coffee_todo3 = Todo()
    coffee_todo3.title = "Turn on"
    coffee_todo3.task = coffee_task

    coffee_todo1.save()
    coffee_todo2.save()
    coffee_todo3.save()


def printIncompleteTasksAndTodos():
    # Jeg filtrere alle tasks for at få dem som indeholder en todo som er incomplete.
    # Jeg prefetcher også alle dens relaterede objekter todos, for at undgå at skulle lave flere queries.
    tasks = Task.objects.filter(todos__complete=False).distinct().prefetch_related(models.Prefetch("todos", to_attr="pre_todos"))

    for task in tasks:
        print(task.name)
        for todo in task.pre_todos:
            print(f"\t{todo.title}")