from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=150)
    gpa = models.FloatField()

    def __str__(self):
        return f'student :{self.first_name} {self.last_name}'
