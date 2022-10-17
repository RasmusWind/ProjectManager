from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('task-list/', views.taskList),
    path('task-detail/<str:pk>/', views.taskDetail),
    path('task-create/', views.taskCreate),
    path('task-update/<str:pk>', views.taskUpdate),
    path('task-delete/<str:pk>', views.taskDelete),

    path('todo-list/', views.todoList),
    path('todo-detail/<str:pk>/', views.todoDetail),
    path('todo-create/', views.todoCreate),
    path('todo-update/<str:pk>', views.todoUpdate),
    path('todo-delete/<str:pk>', views.todoDelete),

    path('team-list/', views.teamList),
    path('team-detail/<str:pk>/', views.teamDetail),
    path('team-create/', views.teamCreate),
    path('team-update/<str:pk>', views.teamUpdate),
    path('team-delete/<str:pk>', views.teamDelete),

    path('worker-list/', views.workerList),
    path('worker-detail/<str:pk>/', views.workerDetail),
    path('worker-create/', views.workerCreate),
    path('worker-update/<str:pk>', views.workerUpdate),
    path('worker-delete/<str:pk>', views.workerDelete),
]