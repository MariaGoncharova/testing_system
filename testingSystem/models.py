# Create your models here.
from django.db import models
from django.utils import timezone


class Variant(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Question(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField()
    right_answer = models.ForeignKey(Variant, related_name='right')

    variants = models.ManyToManyField(Variant)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=128)
    date_create = models.DateTimeField(default=timezone.now)

    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title
