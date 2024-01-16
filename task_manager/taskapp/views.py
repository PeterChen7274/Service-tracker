# taskapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .tasks import check_tasks_job

#主页，显示所有创建的任务
def task_list(request):
    tasks = Task.objects.all()
    check_tasks_job()
    return render(request, 'task_list.html', {'tasks': tasks})

#创建任务
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

#删除任务
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

#续费任务，会重置报警
def extend_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.extended += 1
    task.notified = task.notified_times
    task.save()
    return redirect('task_list')

#修改任务
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.start_time = task.start_time
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

