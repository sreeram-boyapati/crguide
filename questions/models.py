from django.db import models
from django.contrib.auth.models import User
from offices.models import Office
# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=150)
    asked_by = models.ForeignKey(User)
    category = models.ForeignKey(Office)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
    	return str(self.question)


class Answer(models.Model):
    answer_to = models.ForeignKey(Question)
    answered_by = models.ForeignKey(User)
    answer = models.CharField(max_length = 250)
