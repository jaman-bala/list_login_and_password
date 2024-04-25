from django.db import models


class Employee(models.Model):
    title = models.CharField(max_length=55, blank=True)
    login = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    ip_address = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    descriptions = models.TextField(max_length=9999, default='Примичании нет', blank=True)

    class Meta:
        db_table = "employee"
