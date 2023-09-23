from django.urls import path,include
from .views import listTodo,deleteTodo
urlpatterns = [
    path('',listTodo,name='home'),
    path('delete/<int:pk>/',deleteTodo,name='delete'),
    # path('create-todo/',createTodo,name='create')
]