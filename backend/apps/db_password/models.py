from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=15)

    title = models.CharField(max_length=55)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    descriptions = models.TextField(max_length=9999, default='Примичании нет', blank=True)

    class Meta:
        db_table = "employee"