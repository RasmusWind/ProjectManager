from django.shortcuts import render
from .models import Task, Todo, Team, Worker
from django.db import models
from django.db.models import Count, Q
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


def seedWorkers():
    frontend_team = Team.objects.create(name="Frontend")
    backend_team = Team.objects.create(name="Backend")
    testing_team = Team.objects.create(name="Testing")

    w1 = Worker.objects.create(name="Steen Secher")
    w2 = Worker.objects.create(name="Ejvind Møller")
    w3 = Worker.objects.create(name="Konrad Sommer")
    w4 = Worker.objects.create(name="Sofus Lotus")
    w5 = Worker.objects.create(name="Remo Lademann")
    w6 = Worker.objects.create(name="Ella Fanth")
    w7 = Worker.objects.create(name="Anne Dam")
    

    frontend_team.workers.add(w1, w2, w3)
    backend_team.workers.add(w3,w4,w5)
    testing_team.workers.add(w6,w7,w1)





def printIncompleteTasksAndTodos():
    # Jeg filtrere alle tasks for at få dem som indeholder en todo som er incomplete.
    # Jeg prefetcher også alle dens relaterede objekter todos, for at undgå at skulle lave flere queries.
    tasks = Task.objects.filter(todos__complete=False).distinct().prefetch_related(models.Prefetch("todos", to_attr="pre_todos"))

    for task in tasks:
        print(task.name)
        for todo in task.pre_todos:
            print(f"\t{todo.title}")


def printTeamsWithoutTasks():
    teams = Team.objects.filter(current_task=None)
    return teams

def printTeamsAndTasks():
    teams = Team.objects.all().select_related("current_taks")
    for team in teams:
        print(f"{team.name}\t{team.current_task}")

def printTeamsAndTodos():
    teams = Team.objects.all().select_related("current_task").prefetch_related(models.Prefetch("current_task__todos", to_attr="pre_todos"))\
        .annotate(
            complete=Count("current_task__todos", filter=Q(current_task__todos__complete=True)),
            total_todos=Count("current_task__todos")

        )
    
    for team in teams:
        print(f"{team.name}\t{round(team.complete/team.total_todos*100)}%")