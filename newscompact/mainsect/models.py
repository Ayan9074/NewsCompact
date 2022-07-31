from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    preferences = models.CharField(max_length=1000)


class topics(models.Model):
    name = models.CharField(max_length=200)
    websites = models.CharField(max_length=1000)