from django.urls import path

from . import views

urlpatterns = [
    # ex: /tasks/
    path("", views.index, name="index"),
    # ex: /tasks/5/
    path("<int:task_id>/", views.detail, name="detail"),
    # ex: /tasks/5/results/
    path("<int:task_id>/results/", views.results, name="results"),
    # ex: /tasks/5/finish/
    path("<int:task_id>/finish/", views.finish, name="vote"),
]