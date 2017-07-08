from django.test import TestCase
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from django.contrib.auth.models import User

DOCTOR_USERNAME = 'doctor_user1'
DOCTOR_PASSWORD = 'doctor_password1'
DOCTOR_FIRST_NAME = 'Lofton'
DOCTOR_LAST_NAME = 'Bullard'
DOCTOR_EMAIL = 'doctor1@email.com'


class DoctorSerializerTest(TestCase):
    def test_serializer(self):
        doctor_user = User.objects.create(username=DOCTOR_USERNAME,
                                            password=DOCTOR_PASSWORD,
                                            email=DOCTOR_EMAIL)
        doctor = Doctor.objects.create(user=doctor_user,
                                        first_name=DOCTOR_FIRST_NAME,
                                        last_name=DOCTOR_LAST_NAME)
        expected_json = \
            '{{"username": "{0}", "password": "{1}", "email": "{2}", "first_name": "{3}", "last_name": "{4}" }}' \
                .format(DOCTOR_USERNAME,
                        DOCTOR_PASSWORD,
                        DOCTOR_EMAIL,
                        DOCTOR_FIRST_NAME,
                        DOCTOR_LAST_NAME)

        actual_json = DoctorSerializer.serialize(doctor)
        self.assertEqual(expected_json, actual_json)