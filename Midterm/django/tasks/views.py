from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Task

def index(request):
    latest_tasks_list = Task.objects.order_by("-created_at")[:5]
    template = loader.get_template("tasks/index.html")
    context = {
        "latest_tasks_list": latest_tasks_list,
    }
    # output = ", ".join([q.title for q in latest_tasks_list])
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, "tasks/index.html", context)

def detail(request, task_id):
    # try:
    #     task = Task.objects.get(pk=task_id)
    # except Task.DoesNotExist:
    #     raise Http404("task does not exist")
    # return HttpResponse("You're looking at task %s." % task_id)
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})


def results(request, task_id):
    response = "You're looking at the results of task %s."
    return HttpResponse(response % task_id)


def finish(request, task_id):
    return HttpResponse("You're finished task %s." % task_id)