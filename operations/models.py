from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Branch(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


