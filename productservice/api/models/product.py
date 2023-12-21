from django.db import models

# Product Model
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    inventory=models.IntegerField()
    color=models.CharField(max_length=50, choices=(
                                                    ('Black','Black'),
                                                        ('White', 'White'),
                                                        ('Blue', 'Blue'),
                                                        ('Red','Red')
                                                    ), null=True)
    createdate=models.DateTimeField(auto_now=True)
    updatedate=models.DateTimeField(auto_now=True)
