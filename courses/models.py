from django.db import models
from people.models import Faculty


class Undergraduate(models.Model):
    coursename = models.CharField(max_length=50)

    PROGRAM_CHOICES = [
        ('B.Tech. CSE', 'B.Tech. Computer Science and Engineering')
    ]
    programme = models.CharField(choices=PROGRAM_CHOICES, max_length=50)

    SEMESTER_CHOICES = [
        ('I', 'First'),
        ('II', 'Second'),
        ('III', 'Third'),
        ('IV', 'Fourth'),
        ('V', 'Fifth'),
        ('VI', 'Sixth'),
        ('VII', 'Seventh'),
        ('VIII', 'Eighth')
    ]
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20)
    content = models.TextField(max_length=1000)

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science and Engineering Department'),
        ('ECE', 'Electronics and Communication Department'),
        ('MCS', 'Mathematics and Computation Department')
    ]
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    instructor = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.coursename


class Postgraduate(models.Model):
    coursename = models.CharField(max_length=50)

    PROGRAM_CHOICES = [
        ('M.Tech. CSE', 'M.Tech. Computer Science'),
        ('M.Tech. CSIS', 'M.Tech. Computer Science (Information Security)')
    ]
    programme = models.CharField(choices=PROGRAM_CHOICES, max_length=50)

    SEMESTER_CHOICES = [
        ('I', 'First'),
        ('II', 'Second'),
        ('III', 'Third'),
        ('IV', 'Fourth'),
    ]
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=20)
    content = models.TextField(max_length=1000)

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science and Engineering Department'),
        ('ECE', 'Electronics and Communication Department'),
        ('MCS', 'Mathematics and Computation Department')
    ]
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    instructor = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.coursename


class Doctoral(models.Model):
    coursename = models.CharField(max_length=50)
    PROGRAM_CHOICES = [
        ('Ph. D', 'Ph. D.'),
    ]
    programme = models.CharField(choices=PROGRAM_CHOICES, max_length=50)
    content = models.TextField(max_length=1000)

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science and Engineering Department'),
        ('ECE', 'Electronics and Communication Department'),
        ('MCS', 'Mathematics and Computation Department')
    ]
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)

    def __str__(self):
        return self.coursename
