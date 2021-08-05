from django.contrib.auth.models import User
from django.db import models
from users.models import Customer, Suplier, Address
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=255)
    is_sub = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    # has ForeignKey
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child',
                               related_query_name='child')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug, ])


class Product(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField('image', upload_to="Products_image/", null=True, blank=True)
    brand = models.CharField('brand', null=True, blank=True, max_length=255)
    price = models.FloatField('price')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.FloatField('discount',null=True, blank=True)
    # has ForeignKey
    Categories = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    # category = models.ManyToManyField(Category, related_name='products')
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)

    #
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug, ])


class Products_Detail():
    title = models.CharField('title', max_length=255)
    caption = models.TextField(max_length=5000, blank=True)
    quantitiy = models.IntegerField('quantitiy')
    # has OneToOneField
    products = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    text = models.TextField('description', null=True, blank=True)
    rate = models.FloatField(default=5)
    # has ForeignKey
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Tag(models.Model):
    title = models.CharField('title', max_length=255)
    #  has ForeignKey
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Store(models.Model):
    title = models.CharField('title', max_length=255)
    about = models.TextField('about', max_length=2000, blank=True)
    last_update = models.DateField()
    #
    owners = models.ManyToManyField(Suplier)
    #  has ForeignKey
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Cart(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'open'),
        ('CLOSED', 'closed')
    ]

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='open')
    # has ForeignKey
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', related_query_name='cart')


class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    # has ForeignKey
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts', related_query_name='cart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', related_query_name='item')


class Payment(models.Model):
    pay_date = models.DateField()
    total = models.FloatField()
    details = models.TextField('details', max_length=255, blank=True)
    #  has ForeignKey
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.details