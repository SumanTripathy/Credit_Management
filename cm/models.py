from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20, default='')
    current_credit = models.IntegerField()

    def __str__(self):
        return self.name+' | Credit: '+str(self.current_credit)


class history(models.Model):
    senderN = models.CharField(max_length=50)
    receiverN = models.CharField(max_length=50)
    amount = models.IntegerField()
        
    