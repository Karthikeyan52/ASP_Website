from django.db import models
from django.forms import ModelForm


class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(null=False, blank=False, default='')
    contact = models.BigIntegerField()
    subject = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=100, default='')
    object = models.Manager()

    class Meta:
        db_table = "Enquiry"