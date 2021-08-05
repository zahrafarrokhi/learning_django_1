from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Address(models.Model):
    address = models.CharField('address', null=True, blank=True, max_length=255)
    city = models.CharField('city', null=True, blank=True, max_length=255)
    country = models.CharField('country', null=True, blank=True, max_length=255)
    zipcode = models.IntegerField('zipcode', null=True, blank=True)
    fax = models.IntegerField('fax', null=True, blank=True)
    email = models.EmailField('email address', max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField('phone number',null=True, blank=True, )
    # ForeignKey
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Customer(models.Model):
    username = models.CharField('username', max_length=255, unique=True)
    password = models.CharField('password', max_length=255)
    first_name = models.CharField('first name', max_length=50, null=True, blank=True)
    last_name = models.CharField('last name', max_length=50, null=True, blank=True)
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    email = models.EmailField('email address', max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField('phone number',null=True, blank=True, )
    birth_date = models.DateField('birth date', null=True, blank=True)
    picture = models.ImageField(upload_to='profile', null=True, blank=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now, null=True, blank=True)
    is_active = models.BooleanField('active', default=True,
                                    help_text=' whether this user should be treated as active. ')
    # OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.user = self.user.lower()
        return super().save(*args, **kwargs)


class Suplier(models.Model):
    username = models.CharField('username', max_length=255, unique=True)
    password = models.CharField('password', max_length=255)
    first_name = models.CharField('first name', max_length=50, null=True, blank=True)
    last_name = models.CharField('last name', max_length=50, null=True, blank=True)
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    email = models.EmailField('email address', max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField('phone number', null=True, blank=True, )
    birth_date = models.DateField('birth date', null=True, blank=True)
    picture = models.ImageField(upload_to='profile', null=True, blank=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now, null=True, blank=True)
    is_active = models.BooleanField('active', default=True,
                                    help_text=' whether this user should be treated as active. ')
    bank_acconunt = models.CharField(max_length=255, unique=True)
    # OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.user = self.user.lower()
        return super().save(*args, **kwargs)

