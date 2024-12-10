from django.db import models
import datetime

class User(models.Model):
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
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
# class payment_details(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Make sure user is a ForeignKey
#     phone = models.CharField(max_length=13, default='')
#     selected_product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Change this to a ForeignKey
#     amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
#     def __str__(self):
#         return self.user.name

#     class Meta:
#         verbose_name_plural = 'payment_details' 
        
class Resource(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(null=False, blank=False, upload_to='documentation/')

    def __str__(self):
        return self.title
    
    
    
    
    
    
    
    
    
    
    
    
    