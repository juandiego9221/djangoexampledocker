from django.db import models

class Student(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200,blank=True,default='')
    age=models.IntegerField()

    class Meta:
        ordering=('name',)
