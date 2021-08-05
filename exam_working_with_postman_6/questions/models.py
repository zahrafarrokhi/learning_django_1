from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


  
ANSWER_CHOICES = [
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),
]

class Questions(models.Model):
    text = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255, choices=ANSWER_CHOICES)
    # exam = models.ForeignKey(Exam,on_delete = models.CASCADE)  

    def __str__(self):
        return self.text


class Exam(models.Model):
    name = models.CharField(max_length=100)
    date_exam = models.DateTimeField(default = timezone.now)
    questions = models.ManyToManyField(Questions)
    user = models.ForeignKey(User,on_delete = models.CASCADE)  
    marks=models.IntegerField(default=0) 
    status =models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
 
    
class Answers(models.Model):
    answer = models.CharField(max_length=255, choices=ANSWER_CHOICES)
    # user = models.ForeignKey(User,on_delete = models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete = models.CASCADE, null=True)
    question = models.ForeignKey(Questions,on_delete = models.CASCADE) 

    def __str__(self):

        return self.answer
  


# python manage.py makemigrations
# Migrations for 'questions':
#   questions\migrations\0001_initial.py
#     - Create model Questions
#     - Create model Exam
#     - Create model Answers
# *****************************
# python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, questions, sessions
# Running migrations:
#   Applying questions.0001_initial... OK

# ************************************
# https://codereview.stackexchange.com/questions/114962/model-classes-for-a-quiz-app-in-django    
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-in