from django.db import models

from school.models import School


class Student(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='school_student'
    )
    name = models.CharField(max_length=50)
    friend = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name
