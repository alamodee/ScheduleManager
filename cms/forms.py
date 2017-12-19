from django.forms import ModelForm
from cms.models import Schedule, Discussion


class ScheduleForm(ModelForm):
    # Form of schedule
    class Meta:
        model = Schedule
        fields = ('EventName', 'Date', 'Place', 'Note',)


class DiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ('discussion', )