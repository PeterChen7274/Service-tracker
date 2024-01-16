# taskapp/models.py
from django.db import models
from .utils import send_dingtalk_message
from dateutil.relativedelta import relativedelta

class Task(models.Model):
    TYPE_CHOICES = [
        ('url', 'URL'),
        ('ip', 'IP'),
    ]

    type = models.CharField(max_length=3, choices=TYPE_CHOICES) 
    name = models.CharField(max_length=255, unique = True) #任务名字
    start_time = models.DateField() #开始日期
    period_years = models.IntegerField(default=0, verbose_name="Period (Years)") 
    period_months = models.IntegerField(default=0, verbose_name="Period (Months)")
    period_days = models.IntegerField(default=0, verbose_name="Period (Days)") #续费期限，年月日
    ding = models.CharField(max_length=255, default = 'https://oapi.dingtalk.com/robot/send?access_token=858cbe8a1d55ed763ce6e794bb3ff8dcbdc8dc882bd92861ec848e51e1163201') #钉钉机器人链接
    link = models.CharField(max_length=255, default = 'spug.com') #监视IP/url链接
    notified = models.IntegerField(default = 1) 
    notified_times = models.IntegerField(default = 1,  verbose_name="How many times to notify") #报警次数
    created = models.BooleanField(default = False)
    extended = models.IntegerField(default=1)
    note_days = models.IntegerField(default=2, verbose_name = "Days before expire to notice") #提前几天报警

    @property
    def period(self):
        return relativedelta(years=self.period_years, months=self.period_months, days=self.period_days)
    
    @property
    def end_date(self):
        return self.start_time + self.period * self.extended #任务结束日期

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # 创建任务时会收到创建提醒
        if not self.created:
            send_dingtalk_message(self, "Hi, you're now monitoring task " + self.name + "." + "\n" + "At link: " + self.link + ".")
            self.created = True
            self.notified = self.notified_times
            self.save()



