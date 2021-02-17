from django.db import models

# Create your models here.

class Student_detail(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.IntegerField(default=100)
    email = models.EmailField(max_length=254, null=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}-{self.student_id}'