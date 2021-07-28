from django.db import models


# Create your models here.
class Chores(models.Model):
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    user_password = models.CharField(max_length=100, null=False)
    user_chores = models.ForeignKey(Chores, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_name

