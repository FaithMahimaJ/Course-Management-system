from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, default="Unknown")

class courses(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.IntegerField()
    trainer_name=models.CharField(max_length=100,default='Null')
    description=models.CharField(max_length=200,default='Null')
    status=models.BooleanField(default=False)

    


    # def __str__(self):
    #     return self.name
