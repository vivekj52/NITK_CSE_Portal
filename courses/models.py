from django.db import models


class Undergraduate(models.Model):
    coursename = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    department = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)

    def __str__(self):
        return self.coursename


class Postgraduate(models.Model):
    coursename = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    department = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)

    def __str__(self):
        return self.coursename


class Doctoral(models.Model):
    coursename = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.coursename
