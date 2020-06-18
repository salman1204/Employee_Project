from django.db import models


# Create your models here.
from django.db.models import IntegerField


class personal_info(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_birth = models.DateField()
    sex_tup = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]
    sex = models.CharField(max_length=5, choices=sex_tup, default='m')

    def __str__(self):
        return "ID: " + str(self.id) + " Name: " + self.first_name + " " + self.last_name


class job_info(models.Model):
    person = models.OneToOneField(personal_info, on_delete=models.CASCADE)
    job_description_tup =[
        ('sr', 'Sr. Software Eng.'),
        ('mi', 'Software Eng.'),
        ('jr', 'Sr. Software Eng.'),
        ('in', 'Intern Software Eng.'),
    ]
    job_description = models.CharField(max_length=5, choices=job_description_tup, default='sr')
    salary: IntegerField = models.IntegerField()

    def __str__(self):
        return "ID: " + str(self.person.id) + " Salary:" + str(self.salary)

