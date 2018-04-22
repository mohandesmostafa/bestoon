from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    #kharj ro che kasi anjam dade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __unicode__(self):
#        return self.text
        return "{}-{}".format(self.date, self.amount)

#sod bank:
class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    # kharj ro che kasi anjam dade
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __unicode__(self):
        #        return self.text
        return "{}-{}".format(self.date, self.amount)

