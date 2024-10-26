from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by("-created_at")
    template = loader.get_template("tasks/index.html")
    context = {
        "latest_tasks_list": latest_tasks_list,
    }
    return render(request, "tasks/index.html", context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})

def finish(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return render(request, "tasks/finished.html", {"task": task})

def incomplete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = False
    task.save()
    return render(request, "tasks/incompleted.html", {"task": task})

def create(request):
    return render(request, "tasks/task_form.html")

def created(request):
    if request.method == "GET":
        title = request.GET.get("title")
        description = request.GET.get("description")
        completed = request.GET.get("completed")
        if completed == None:
            completed = False
        else:
            completed = True
        task = Task(title = title, description = description, created_at = timezone.now(), completed = completed)
        task.save()
        return redirect("/tasks/")

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/task_form.html", {"task": task})

def edited(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id)
        task.title = request.GET.get("title")
        task.description = request.GET.get("description")
        completed = request.GET.get("completed")
        if completed == None:
            task.completed = False
        else:
            task.completed = True
        # task = Task(title = title, description = description, created_at = timezone.now(), completed = completed)
        task.save()
        # return render(request, "tasks/detail.html", {"task": task})
        return redirect("/tasks/")


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("/tasks/")