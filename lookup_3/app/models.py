from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
	#fk related_query_name='item'
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='items',related_query_name='item')
	# mtm
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    mod_date = models.DateField(null=True,blank=True)    
    number_of_comments = models.IntegerField(null=True,blank=True)
    number_of_pingbacks = models.IntegerField(null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.headline