from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Doctor(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patients = models.ManyToManyField(Patient, related_name='doctors')

    def __str__(self):
        return 'Dr. {} {}'.format(self.first_name, self.last_name)
