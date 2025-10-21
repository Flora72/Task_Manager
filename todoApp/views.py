# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm


def index(request):
    return render(request, 'index.html')

def todo_list(request):
    return render(request, 'todo_list.html')

# creates the task

def create_task(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        else:
            form = ListForm()
    return render(request, 'todo_form.html', {'form': form})


# updates the saved tasks
def update_task(request, task_id):
    task = get_object_or_404(List, id=task_id)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        else:
            form = ListForm(instance=task)
    return render(request, 'todo_form.html', {'form': form})

# deletes the saved or completed tasks
def delete_task(request, task_id):
    task = get_object_or_404(List, id=task_id)
    task.delete()
    return redirect('todo_list')