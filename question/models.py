from django.db import models




class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    topic = models.CharField(max_length=400)
    question = models.TextField()



    def __str__ (self):
        return self.name

# Create your models here.
