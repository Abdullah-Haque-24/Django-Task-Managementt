from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:        
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {"form" : task_form})


# Edit task
def edit_task(request, id):
    task = models.Task.objects.get(id=id) #here the name of the pk and id, id is fixed
    task_form = forms.TaskForm(instance=task)
    # print(task.title)
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    return render(request, 'add_task.html', {"form" : task_form})

#Delete task
def delete_task(request, id):
    task = models.Task.objects.get(id=id)
    task.delete()
    return redirect('homepage')