# tasks.py
from apscheduler.schedulers.background import BackgroundScheduler
from .utils import send_dingtalk_message
from .models import Task
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.executors.pool import ThreadPoolExecutor

#定期向所有即将过期的任务发报警信息
def check_tasks_job():
    all_tasks = Task.objects.all()
    tasks_to_notify = [task for task in all_tasks if task.notified > 0 and task.end_date <= timezone.now().date() + timezone.timedelta(days=task.note_days)]
    for task in tasks_to_notify:
        send_dingtalk_message(task, f"Task '{task.name}' ends in less than {task.note_days} days. Link: {task.link}")
        task.notified -= 1
        task.save()


executors = {
    'default': ThreadPoolExecutor(10),  
}

scheduler = BackgroundScheduler(executors=executors)
scheduler.add_job(check_tasks_job, trigger=IntervalTrigger(seconds=40000)) #修改检测间隔，40000秒约为半天
scheduler.start()




