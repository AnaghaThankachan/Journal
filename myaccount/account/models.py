from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    particulars=models.CharField(max_length=100)
    date=models.DateField()
    amount=models.IntegerField(default=0)
    ttype=models.IntegerField(default=1)