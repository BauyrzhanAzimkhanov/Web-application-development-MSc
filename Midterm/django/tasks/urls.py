from django.urls import path

from . import views

urlpatterns = [
    # ex: /tasks/
    path("", views.index, name="index"),
    # ex: /tasks/5/
    path("<int:task_id>/", views.detail, name="detail"),
    # ex: /tasks/5/edit/
    path("<int:task_id>/edit/", views.edit, name="edit"),
    # ex: /tasks/5/edited/
    path("<int:task_id>/edited/", views.edited, name="edited"),
    # ex: /tasks/5/finish/
    path("<int:task_id>/finish/", views.finish, name="finish"),
    # ex: /tasks/5/incomplete/
    path("<int:task_id>/incomplete/", views.incomplete, name="incomplete"),
    # ex: /tasks/create/
    path("create/", views.create, name="create"),
    # ex: /tasks/created/
    path("created/", views.created, name="created"),
    # ex: /tasks/5/delete/
    path("<int:task_id>/delete/", views.delete, name="delete"),
]