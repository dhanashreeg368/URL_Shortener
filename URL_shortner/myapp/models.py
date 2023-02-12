from django.db import models

# Create your models here.
# models is same as table

#creating database here 
class LongtoShort(models.Model):
    long_url = models.URLField(max_length=500) #making fields here #column names 
    short_url = models.CharField(max_length=50, unique = True) #value should be unique
    date = models.DateField(auto_now_add= True) #automatically add date
    clicks = models.IntegerField(default=0)



