from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Task, Todo, Team, Worker
from api.serializers import TaskSerializer, TodoSerializer, TeamSerializer, WorkerSerializer

@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        'TaskList':'/task-list/',
        'TaskDetail':'/task-detail/<str:pk>/',
        'TaskCreate':'/tast-create/',
        'TaskUpdate':'/tast-update/<str:pk>/',
        'TaskDelete':'/tast-delete/<str:pk>/',

        'TodoList':'/todo-list/',
        'TodoDetail':'/todo-detail/<str:pk>/',
        'TodoCreate':'/todo-create/',
        'TodoUpdate':'/todo-update/<str:pk>/',
        'TodoDelete':'/todo-delete/<str:pk>/',

        'TeamList':'/team-list/',
        'TeamDetail':'/team-detail/<str:pk>/',
        'TeamCreate':'/team-create/',
        'TeamUpdate':'/team-update/<str:pk>/',
        'TeamDelete':'/team-delete/<str:pk>/',

        'WorkerList':'/worker-list/',
        'WorkerDetail':'/worker-detail/<str:pk>/',
        'WorkerCreate':'/worker-create/',
        'WorkerUpdate':'/worker-update/<str:pk>/',
        'WorkerDelete':'/worker-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.filter(pk=pk)
    tasks.delete()
    return Response("Task successfully deleted!")

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.filter(pk=pk)
    todo.delete()
    return Response("Task successfully deleted!")


@api_view(['GET'])
def teamList(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def teamDetail(request, pk):
    team = Team.objects.get(pk=pk)
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def teamCreate(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def teamUpdate(request, pk):
    team = Team.objects.get(pk=pk)
    serializer = TeamSerializer(instance=team, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def teamDelete(request, pk):
    team = Team.objects.filter(pk=pk)
    team.delete()
    return Response("Task successfully deleted!")


@api_view(['GET'])
def workerList(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workerDetail(request, pk):
    worker = Worker.objects.get(pk=pk)
    serializer = WorkerSerializer(worker, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def workerCreate(request):
    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def workerUpdate(request, pk):
    worker = Worker.objects.get(pk=pk)
    serializer = WorkerSerializer(instance=worker, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def workerDelete(request, pk):
    worker = Worker.objects.filter(pk=pk)
    worker.delete()
    return Response("Task successfully deleted!")