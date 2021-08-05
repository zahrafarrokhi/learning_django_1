from django.contrib.auth.models import User
from django.db import models
# django.utils
from django.utils import timezone
from django.utils.text import slugify

from django.urls import reverse

class PublishedArticlesManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='puplish')


class Article(models.Model):
    STATUS =(
        ('draft','Draft'),
        ('puplish','Puplish'),

    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True,null=True,blank=True)
    body = models.TextField()
    publish= models.DateTimeField(default=timezone.now)       
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS,default ='draft')
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    objects = models.Manager()
    puplished = PublishedArticlesManager()
    

    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):        
        if not self.slug:
            self.slug = slugify(self.title,allow_unicode =True)
        return super().save(*args,**kwargs)
    
    
    # def get_absolute_url(self):
    #     return reverse('blog:article_detail', kwargs={'id:'self.id,'slug': self.slug})

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.id, self.slug])
		
   
   