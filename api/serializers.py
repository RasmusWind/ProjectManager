from rest_framework import serializers
from django.db.models import Model
from project.models import Task, Todo, Worker, Team
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path

class CRUD:
    def __init__(self, model:Model, modelserializer:serializers.ModelSerializer):
        self.model = model
        self.modelserilizer = modelserializer

    @api_view(["GET"])
    def getOverview(self, request):
        return Response({
            f"{self.model.__name__}List":f"/{self.model.__name__}-list/",
            f"{self.model.__name__}Detail":f"/{self.model.__name__}-detail/<str:pk>/",
            f"{self.model.__name__}Create":f"/{self.model.__name__}-create/",
            f"{self.model.__name__}Update":f"/{self.model.__name__}-update/<str:pk>/",
            f"{self.model.__name__}Delete":f"/{self.model.__name__}-delete/<str:pk>/",
        })

    @staticmethod
    @api_view(['GET'])
    def getList(self, request):
        items = self.model.objects.all()
        serializer = self.modelserilizer(items, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def getDetail(self, request, pk):
        items = self.model.objects.get(pk=pk)
        serializer = self.modelserilizer(items, many=False)
        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    def postCreate(self, request):
        serializer = self.modelserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    def postUpdate(self, request, pk):
        items = self.model.objects.get(pk=pk)
        serializer = self.modelserilizer(instance=items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['DELETE'])
    def deleteDelete(self, request, pk):
        items = self.model.objects.filter(pk=pk)
        items.delete()
        return Response(f"{self.model.__name__} successfully deleted!")

    def paths(self):
        return [
            path(f"{self.model.__name__}-list/", lambda request: self.getList(self, request)),
            path(f"{self.model.__name__}-detail/<str:pk>/", lambda request, pk:self.getDetail(self, request, pk)),
            path(f"{self.model.__name__}-create/", lambda request: self.postCreate(self, request)),
            path(f"{self.model.__name__}-update/<str:pk>/", lambda request, pk: self.postUpdate(self, request, pk)),
            path(f"{self.model.__name__}-delete/<str:pk>/", lambda request, pk: self.deleteDelete(self, request, pk)),
        ]
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'