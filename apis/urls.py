
from django.urls import path
from apis.views import todo

urlpatterns = [

    path("todo", todo.GetToDoAPIView.as_view(), name="get_todo"),
    path("todo/create", todo.CreateToDoAPIView.as_view(), name="create_todo"),
    path("todo/edit/<int:id>", todo.EditToDoAPIView.as_view(), name="edit_todo"),
    path("todo/delete/<int:id>", todo.DeleteToDoAPIView.as_view(), name="delete_todo"),

]
