from django.db import models

# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=255, null=True,blank=True) 
    mobile = models.BigIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.first_name
    
# create a model in models.py file 
# model_name : ---> Category
class Category(models.Model):
       cat_name = models.CharField(max_length =50 ,null=True,blank=True)
       cat_image = models.ImageField(upload_to='category/')
       
       
       def __str__(self):
           return self.cat_name 
       
       
       
class Product(models.Model):
    pro_name = models.CharField(max_length=50, null=True)
    pro_price = models.IntegerField(max_length=50, null=True)
    pro_description = models.TextField(max_length=100, null=True)
    pro_image = models.ImageField(max_length=100, null=True)
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    
    
    
    def __str__(self):
        return self.pro_name  
    
class Order(models.Model):
    address = models.CharField(max_length=200,default='0',null=True)
    mobile = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    customer = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.pro_name
    