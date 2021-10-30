from django.db import models

class Signin(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=12)


    def __str__(self):
        return self.name