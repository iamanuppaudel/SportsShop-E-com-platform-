from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.name:
            name= self.name
        else:
            name= self.device
        return str(name)

class clubname(models.Model):
    club_name = models.CharField(max_length=50)
    def __str__(self):
        return self.club_name

class category(models.Model):
    category_name = models.CharField(null= True, blank= True,max_length=50)

    def __str__(self):
        return self.category_name


class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null= True, blank= True)
    price = models.FloatField(null= True, blank= True)
    before_price = models.FloatField(null= True, blank= True)
    image = models.ImageField(blank=True, null=True)
    club = models.ForeignKey(clubname, on_delete=models.SET_NULL,null= True, blank= True)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(blank=True, null= True, default=timezone.now)
    relatedproducts = models.ManyToManyField('self', blank=True, null= True)
    hot_deal = models.BooleanField(default=False, null= True, blank= True)
    in_stock =  models.BooleanField(default=True, null= True, blank= True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default= False, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    Product = models.ForeignKey(product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product.name

    @property
    def get_total(self):
        total = self.Product.price * self.quantity
        return total



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    phone= models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    order_notes= models.TextField(blank=True, null= True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    

class blog(models.Model):
    writer_name = models.CharField(max_length=100, null=True, blank=True)
    blog_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    thumbnail_picture = models.ImageField(blank=True, null=True)
    title = models.TextField(null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    view_count = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.thumbnail_picture.url
        except:
            url =''
        return url
