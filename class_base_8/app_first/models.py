from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    puplished = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True,allow_unicode=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,related_name='tcomments')
    name = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return f'{self.name} {self.body[0:2]}'