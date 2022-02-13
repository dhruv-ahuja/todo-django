from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("confirm/<int:pk>", views.confirm_deletion, name="confirm_deletion"),
    path("delete/<int:pk>", views.delete_todo, name="delete_todo"),
    path("update/<int:pk>", views.complete_todo, name="complete_todo"),
]
