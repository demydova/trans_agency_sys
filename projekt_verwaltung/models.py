

from django.db import models
from datetime import datetime




# Create your models here.

class Client(models.Model):
    login = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    fn = models.CharField(max_length=30)
    ln = models.CharField(max_length=30)
    firm = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    telefon = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.login)


class Translator(models.Model):
    login = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    fn = models.CharField(max_length=30)
    ln = models.CharField(max_length=30)
    mother_language = models.CharField(max_length=30)
    trans_language = models.CharField(max_length=30)
    telefon = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.login)



class Project(models.Model):
    description = models.CharField(max_length=100, blank=True)
    client = models.ForeignKey(Client)
    translator = models.ManyToManyField(Translator)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(default=datetime.now, blank=True)
    src_language = models.CharField(max_length=100, default="German")
    target_language = models.CharField(max_length=100, default="Russian")
    pages_number = models.FloatField(default=0.0)
    page_rate = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    paid= models.CharField( default=0.0, max_length=100, blank=True)
    invoice=models.CharField(max_length=30,default="invoice-0001_2015")
    notice=models.CharField(default="unpaid",max_length=100,blank=True)

    def __str__(self):
        return self.description

