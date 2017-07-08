from django.test import TestCase
from django.contrib.auth.models import User
from patients.models import Patient

PATIENT_USERNAME = 'patient_user1'
PATIENT_PASSWORD = 'patient_password1'
PATIENT_FIRST_NAME = 'John'
PATIENT_LAST_NAME = 'Doe'
PATIENT_EMAIL = 'patient1@email.com'


class PatientModelTest(TestCase):

    def test_create_patient(self):
        patient_user = User.objects.create(username=PATIENT_USERNAME,
                                           password=PATIENT_PASSWORD,
                                           email=PATIENT_EMAIL)
        patient = Patient.objects.create(user=patient_user,
                                         first_name=PATIENT_FIRST_NAME,
                                         last_name=PATIENT_LAST_NAME)

        patient.save()

        patient = Patient.objects.filter(user=patient_user)
        self.assertEqual(len(patient), 1)

        patient = patient[0]

        self.assertEqual(patient.user.username, PATIENT_USERNAME)
        self.assertEqual(patient.user.password, PATIENT_PASSWORD)
        self.assertEqual(patient.user.email, PATIENT_EMAIL)
        self.assertEqual(patient.first_name, PATIENT_FIRST_NAME)
        self.assertEqual(patient.last_name, PATIENT_LAST_NAME)
