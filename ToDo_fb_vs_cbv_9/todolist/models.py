from django.db import models
from django.utils.text import slugify
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    slug = models.SlugField(max_length=150,unique=True,null=True,blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

