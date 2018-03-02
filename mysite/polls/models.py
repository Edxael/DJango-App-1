from django.db import models



# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



class Choise(models.Model):
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeingKey(Question, on_delete=models.CASCADE)