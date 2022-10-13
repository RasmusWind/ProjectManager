from django.urls import path
from django.http import HttpResponse

def index():
    return HttpResponse("<h1>Hello World!</h1>")

urlpatterns = [
    path(r'', index, name="index"),
]