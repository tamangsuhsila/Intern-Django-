from django.db import models



# Create your models here.


class product(models.Model):
    product_name=models.CharField(max_length=100)
    description=models.TextField()
    stock=models.IntegerField(default=100)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    
    image=models.ImageField(upload_to='static/product',blank=True)

    season= models.CharField(max_length=100, choices=(('winter','W'),
                                                      ('summer','S'),
                                                      ('monsoon','M')))
    gender = models.CharField(max_length=100, choices=(('male','M'),
                                                       ('female','F')))
    
    size = models.CharField(max_length=100, choices=(('38','38'),
                                                     ('39','39'),
                                                     ('40','40'),
                                                     ))
    
    discount = models.IntegerField()
    
    def __str__(self):
        return self.product_name
    
    
