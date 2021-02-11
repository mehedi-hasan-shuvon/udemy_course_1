from django.db import models

# Create your models here.
class Book(models.Model):
    STATUSES =(
        (0,'Unknown'),
        (1,'processed'),
        (2,'paid'),
    )
    title=models.CharField(max_length=36,blank=False,unique=True,default='',choices=STATUSES)
    #blank=true means this field can not be blanked and unique=true is slef explainatory
    #here choices takes a tuple and it meands  we can only pick the those choices only
