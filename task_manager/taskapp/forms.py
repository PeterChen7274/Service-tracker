# taskapp/forms.py
from django import forms
from .models import Task

class DurationWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.NumberInput(attrs={'min': '0', 'step': '1'}),
                   forms.NumberInput(attrs={'min': '0', 'step': '1'}))
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value // 12, value % 12]
        return [0, 0]

class DurationField(forms.MultiValueField):
    widget = DurationWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return data_list[0] * 12 + data_list[1]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created', 'notified', 'end_date']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'date'}),
            'period_years': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'period_months': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'period_days': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
        }
        input_formats = {
            'start_time': ['%Y-%m-%d'],
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            del self.fields['start_time'] # 初始日期不可修改，如想修改可以删掉这行

