from django.db import models

# Create your models here.


class Trainees(models.Model):
    names = models.CharField(max_length=100, null=True, blank=False)
    email = models.CharField(max_length=100, null=True, blank=False)
    username = models.CharField(max_length=100, null=True, blank=False)
    dob = models.DateField()
    location = models.CharField(max_length=100, null=True, blank=False)

    # def __str__(self):
    # return self.names, self.location

    class Meta:
        db_table = "trainees"
