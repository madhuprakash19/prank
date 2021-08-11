from django.db import models
from django.urls import reverse

class CreateUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail',kwargs={'pk':self.pk})

class PrankList(models.Model):
    yourName = models.CharField(max_length=50)
    crushName = models.CharField(max_length=50)
    prankster = models.ForeignKey('crush.CreateUser',related_name='prankster_name',on_delete=models.CASCADE)

    def __str__(self):
        return self.yourName
