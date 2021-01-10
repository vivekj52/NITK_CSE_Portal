from django.db import models
from people.models import Faculty
from django.utils.timezone import localdate


class Workshops(models.Model):

    title = models.CharField(max_length=500)

    STATUS_CHOICES = [
        ('UP', 'Upcoming'),
        ('C', 'Completed')
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)

    from_date = models.DateField(default=localdate)
    to_date = models.DateField(default=localdate)
    organizers = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Conferences(models.Model):

    title = models.CharField(max_length=500)
    STATUS_CHOICES = [
        ('UP', 'Upcoming'),
        ('C', 'Completed')
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    sponsored = models.CharField(max_length=50)

    from_date = models.DateField(default=localdate)
    to_date = models.DateField(default=localdate)
    organizers = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=100)
    website_link = models.CharField(max_length=100)
    cfp = models.CharField(max_length=50)
    paper_submission_de = models.DateField(default=localdate)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
