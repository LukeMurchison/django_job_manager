from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.


class Paper(models.Model):
    paper_name = models.CharField(max_length=200)
    cost = models.FloatField()

    def __str__(self):
        return self.paper_name

    def get_absolute_url(self):
        return reverse('post_paper_detail', args=[str(self.id)])
    


class Job(models.Model):
    job_name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    start_time = models.DateField()
    end_time = models.DateField()
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    copies = models.IntegerField()
    sides = models.IntegerField()
    oversized = models.BooleanField()
    color = models.BooleanField()
    mark_up = models.FloatField()
    finishing = models.FloatField()
    package = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

