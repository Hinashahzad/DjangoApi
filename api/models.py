from django.db import models

# Create your models here.
#MODEL: 1 Product
class Product (models.Model):
    product_id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50, null =True)
    about=models.TextField(max_length=100, null=True)

    product_description=models.TextField(default=None, null =True)
    type=models.CharField(max_length=100, choices=(
        ("Eastern", "Eastern"), 
        ("Western", "Western")
    ))
    added_date=models.DateTimeField(auto_now=True, null =True)
