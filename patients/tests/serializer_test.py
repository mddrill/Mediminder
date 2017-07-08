from django.test import TestCase
from doctors.models import Doctor
from patients.serializers import PatientSerializer
from django.contrib.auth.models import User

PATIENT_USERNAME = 'patient_user1'
PATIENT_PASSWORD = 'patient_password1'
PATIENT_FIRST_NAME = 'John'
PATIENT_LAST_NAME = 'Doe'
PATIENT_EMAIL = 'patient1@email.com'


class PatientSerializerTest(TestCase):
    def test_serializer(self):
        doctor_user = User.objects.create(username=PATIENT_USERNAME,
                                            password=PATIENT_PASSWORD,
                                            email=PATIENT_EMAIL)
        doctor = Doctor.objects.create(user=doctor_user,
                                        first_name=PATIENT_FIRST_NAME,
                                        last_name=PATIENT_LAST_NAME)
        expected_json = \
        '{{"username": "{0}", "password": "{1}", "email": "{2}", "first_name": "{3}", "last_name": "{4}" }}' \
            .format(PATIENT_USERNAME,
                    PATIENT_PASSWORD,
                    PATIENT_EMAIL,
                    PATIENT_FIRST_NAME,
                    PATIENT_LAST_NAME)

        actual_json = PatientSerializer.serialize(doctor)
        self.assertEqual(expected_json, actual_json)