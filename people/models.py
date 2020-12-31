from django.db import models
from django.utils.timezone import localdate


class Faculty(models.Model):
    name = models.CharField(max_length=50)
    DESIGNATION_CHOICES = [('PR', 'PROFESSOR'),
                           ('HOD', 'HEAD OF DEPARTMENT'),
                           ('AP', 'ASSOCIATE PROFESSOR'),
                           ('AS', 'ASSISTANT PROFESSOR'),
                           ('AF', 'ADJUNCT FACULTY'),
                           ('TL', 'TEMPORARY LECTURER')]
    designation = models.CharField(choices=DESIGNATION_CHOICES, max_length=20)
    joining_date = models.DateField(default=localdate)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20)
    academic_background = models.TextField(max_length=500, default='')
    area_of_interest = models.TextField(max_length=200, default='')

    def __str__(self):
        return 'Name: ' + self.name + 'Designation: ' + self.designation


class Staff(models.Model):
    name = models.CharField(max_length=50)
    ROLES_CHOICES = [('AM', 'ASSISTANT MECHANIC'),
                     ('AP', 'ASSISTANT PROGRAMMER'),
                     ('TO', 'TECHNICAL OFFICER'),
                     ('LA', 'LAB ASSISTANT')]
    role = models.CharField(choices=ROLES_CHOICES, max_length=20)

    def __str__(self):
        return 'Name: ' + self.role + 'Role: ' + self.role


class ProjectStaff(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    project = models.TextField(max_length=100)

    def __str__(self):
        return 'Name: ' + self.name
