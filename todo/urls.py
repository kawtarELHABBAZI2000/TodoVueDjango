from django.urls import path

from .views import (
    ListCreateTodo,
    Login,
    RetrieveUpdateDestroyTodo
)

urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('list-create-todo/', ListCreateTodo.as_view(), name = 'list-create-todo'),
    path('retrieve-update-destroy-todo/<int:pk>/', RetrieveUpdateDestroyTodo.as_view(), name = 'retrieve-update-destroy'),
    
]
