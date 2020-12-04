from django.db import models




class Content(models.Model):
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField()
    date = models.DateField()
    time = models.TimeField()
    question = models.TextField(default='')

    def __str__ (self):
        return self.subject

class Answer(models.Model):
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    answer = models.TextField(default='')

    def __str__ (self):
        return self.subject
# Create your models here.
