from django.db import models

# Create your models here.

class Report(models.Model):
    attacked_date = models.DateTimeField()
    attacked_agent = models.CharField(max_length=64)
    agent_level = models.IntegerField(default=0)
    damaged_type = models.CharField(max_length=16)
    attacker = models.CharField(max_length=64)
    attacked_portal = models.CharField(max_length=128)
    linked_portal = models.CharField(max_length=128)
    portal_owner = models.CharField(max_length=64)
    portal_address = models.CharField(max_length=256)
    portal_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    portal_longtitude = models.DecimalField(max_digits=9, decimal_places=6)

class Portal(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=128)