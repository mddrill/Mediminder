from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Instruction(models.Model):
    given_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, related_name='instructions_given')
    patient = models.ForeignKey(Patient, related_name='instructions_recieved', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ('given_at', )

