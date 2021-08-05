from django.db import models


# Create your models here.
class Chores(models.Model):
    name = models.CharField(max_length=250, null=True, default='+25')
    create_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30, null=True)
    complete = models.PositiveSmallIntegerField(default=0)



    def __str__(self):
        return self.name
