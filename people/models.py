from django.db import models
from django.utils.timezone import localdate
from django.contrib.auth.models import User


class Faculty(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    DESIGNATION_CHOICES = [('PR', 'PROFESSOR'),
                           ('HOD', 'HEAD OF DEPARTMENT'),
                           ('AP', 'ASSOCIATE PROFESSOR'),
                           ('AS', 'ASSISTANT PROFESSOR'),
                           ('AF', 'ADJUNCT FACULTY'),
                           ('TL', 'TEMPORARY LECTURER')]
    designation = models.CharField(choices=DESIGNATION_CHOICES, max_length=20)
    joining_date = models.DateField(default=localdate)
    phone = models.CharField(max_length=20)
    academic_background = models.TextField(max_length=500, default='')
    area_of_interest = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Staff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ROLES_CHOICES = [('AM', 'ASSISTANT MECHANIC'),
                     ('AP', 'ASSISTANT PROGRAMMER'),
                     ('TO', 'TECHNICAL OFFICER'),
                     ('LA', 'LAB ASSISTANT')]
    role = models.CharField(choices=ROLES_CHOICES, max_length=20)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class ProjectStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20)
    project = models.TextField(max_length=100)
    area_of_interest = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
