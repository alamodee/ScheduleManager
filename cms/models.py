from django.db import models

# Create your models here.
class Schedule(models.Model):
    EventName = models.CharField(max_length=20)
    Date = models.IntegerField()
    Place = models.CharField(max_length=20)
    Note = models.CharField(max_length=40)



class Discussion(models.Model):
    schedule = models.ForeignKey(Schedule, verbose_name='Schedule', related_name='discussions')
    discussion = models.TextField('Discussion', blank=True)

    def __str__(self):
        return self.discussion
