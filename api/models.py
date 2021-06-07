from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    classs = models.CharField(max_length=100)
    math = models.IntegerField()
    sci = models.IntegerField()
    boi = models.IntegerField()

    def total_marks():
        pass 
    

    def __str__(self):
        return self.name