from django.db import models
from django.utils import timezone
# from django.conf import settings

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
    
# class User(models.Model):
#     user=models.CharField(max_length=100)
    
class Post(models.Model):
    
    options = (
        ('draft','Draft'),
        ('published', 'Published')
    )
    title = models.TextField()
    publish = models. DateTimeField(default=timezone.now)
    author = models.CharField(max_length=255)
    content = models.TextField()
    status = models. CharField(max_length=10, choices=options, default='draft')
    image = models. ImageField(upload_to='static/blog', blank=True)
    created_at = models .DateTimeField(auto_now_add= True)
    updated_to = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['publish']
        
    def __str__(self):
        return self.title