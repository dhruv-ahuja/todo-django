from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>", views.confirm_deletion, name="confirm_deletion"),
    path("update/<int:pk>", views.complete_todo, name="complete_todo"),
]
