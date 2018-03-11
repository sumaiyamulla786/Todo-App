from django.db import models
from django.contrib.auth.models import User
#from django_mysql.models import ListCharField

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.CharField(max_length=500,default=None,null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True,null=True)
    creater = models.ForeignKey(User,default=None,null=True,on_delete=models.CASCADE,)
    #add in author later
    def __str__(self):
        return self.title

