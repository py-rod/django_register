from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, TaskCreateForm
from .models import Task

# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if (
            form.is_valid()
            and User.objects.filter(email=request.POST["email"]).exists() == False
        ):
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "regis.html", {"form": form})


def loginsession(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "User or password is incorrect",
                },
            )
        else:
            login(request, user)
            return redirect("task")

        return render(request, "login.html", {"form": AuthenticationForm})

@login_required()
def closession(request):
    logout(request)
    return redirect("home")

@login_required()
def task(request):
    task = Task.objects.filter(user=request.user)
    return render(request, "task.html",  {
        "tasks": task
    })
    
@login_required()   
def CreateTask(request):
    if request.method == "GET":
        return render(request, 'createtask.html', {
            "form": TaskCreateForm 
        })
    else:
        try:
            form = TaskCreateForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("task")
        except ValueError:
            return render(request, "createtask.html", {
                "form": TaskCreateForm,
                "error": "Put data value"
            })
  
@login_required()         
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskCreateForm(instance=task)
        return render(request, "taskdetail.html", {
            "task": task,
            "form": form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskCreateForm(request.POST, instance=task)
            form.save()
            return redirect("task")
        except ValueError:
            return render(request, "taskdetail.html", {
                "task": task,
                "form": form,
                "error": "Error updating task :("
            })
        
@login_required()     
def task_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datecomplete = timezone.now()
        task.save()
        return redirect("task")
    
@login_required()
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        task = Task.objects.filter(user=request.user)
        return render(request, "task.html",  {
            "tasks": task
        })