# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    otch = models.CharField(max_length=50)
    dater = models.DateField()
    passport = models.CharField(max_length=15)

    def user_name(self):
        return self.fam + ' ' + self.name[0] + '. ' + self.otch[0] + '.'


class Request(models.Model):
    user = models.ForeignKey(User)
    opis = models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    tele = models.CharField(max_length=50)


class Product (models.Model):
    request = models.ForeignKey(Request)
    naimen = models.CharField(max_length=50)
    kolich = models.FloatField()
    edinic = models.CharField(max_length=20)
    cost = models.FloatField()