from django.db import models

# Create your models here.
#MODEL: 1 Product
class Product (models.Model):
    product_id: models.AutoField(primary_key=True)
    product_name:models.CharField(max_length=50)
    product_description:models.TextField()
    type=models.CharField(max_length=100, choices=(
        ("Eastern", "Eastern"), 
        ("Western", "Western")
    ))
    product_added_date=models.DateTimeField(auto_now=True)
