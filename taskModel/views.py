from django.shortcuts import render, redirect
from . import forms
from . import models
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect(add_task) 
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    edit_form = forms.TaskForm(instance=task)
    
    if request.method == 'POST': 
        edit_form = forms.TaskForm(request.POST, instance=task) 
        if edit_form.is_valid(): 
            edit_form.save()
            return redirect('homepage')
    
    return render(request, 'add_task.html', {'form' : edit_form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')