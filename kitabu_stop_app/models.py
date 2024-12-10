from django.db import models
import datetime

class user(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    phone = models.CharField(max_length=13, default='')
    email=models.EmailField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'    
    
#product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
     #salestuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return self.name  
    
    
#customer orders
# class Order(models.Model):
#     #select the product
#     product =models.ForeignKey(Product, on_delete=models.CASCADE)
#     #who is the customer
#     user = models.ForeignKey(user, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     address = models.CharField(max_length=100, default='', blank=True)
#     phone = models.CharField(max_length=13, default='', blank=True)
#     date = models.DateField(default=datetime.datetime.today)
#     status = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.product.name
    
class Contact(models.Model):
    name =  name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    