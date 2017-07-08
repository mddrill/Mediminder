from django.test import TestCase
from django.contrib.auth.models import User
from doctors.models import Doctor
from patients.models import Patient

DOCTOR_USERNAME = 'doctor_user1'
DOCTOR_PASSWORD = 'doctor_password1'
DOCTOR_FIRST_NAME = 'Lofton'
DOCTOR_LAST_NAME = 'Bullard'
DOCTOR_EMAIL = 'doctor1@email.com'

PATIENT_USERNAME = 'patient_user1'
PATIENT_PASSWORD = 'patient_password1'
PATIENT_FIRST_NAME = 'John'
PATIENT_LAST_NAME = 'Doe'
PATIENT_EMAIL = 'patient1@email.com'

PATIENT_USERNAME2 = 'patient_user2'
PATIENT_PASSWORD2 = 'patient_password2'
PATIENT_FIRST_NAME2 = 'Joe'
PATIENT_LAST_NAME2 = 'Sixpack'
PATIENT_EMAIL2 = 'patient2@email.com'

class DoctorModelTest(TestCase):

    def test_create_doctor(self):
        doctor_user = User.objects.create(username=DOCTOR_USERNAME,
                                          password=DOCTOR_PASSWORD,
                                          email=DOCTOR_EMAIL)
        doctor = Doctor.objects.create(user=doctor_user,
                                       first_name=DOCTOR_FIRST_NAME,
                                       last_name=DOCTOR_LAST_NAME)
        doctor.save()

        doctor = Doctor.objects.filter(user=doctor_user)
        self.assertEqual(len(doctor), 1)
        doctor = doctor[0]

        self.assertEqual(doctor.user.username, doctor_user.username)
        self.assertEqual(doctor.user.password, doctor_user.password)
        self.assertEqual(doctor.user.email, doctor_user.email)
        self.assertEqual(doctor.first_name, DOCTOR_FIRST_NAME)
        self.assertEqual(doctor.last_name, DOCTOR_LAST_NAME)

    def test_add_patients_to_doctor(self):
        doctor_user = User.objects.create(username=DOCTOR_USERNAME,
                                          password=DOCTOR_PASSWORD,
                                          email=DOCTOR_EMAIL)
        doctor = Doctor.objects.create(user=doctor_user,
                                        first_name=DOCTOR_FIRST_NAME,
                                        last_name=DOCTOR_LAST_NAME)
        doctor.save()

        patient_user = User.objects.create(username=PATIENT_USERNAME,
                                           password=PATIENT_PASSWORD,
                                           email=PATIENT_EMAIL)
        patient = Patient.objects.create(user=patient_user,
                                         first_name=PATIENT_FIRST_NAME,
                                         last_name=PATIENT_LAST_NAME)

        patient.save()
        patient_user2 = User.objects.create(username=PATIENT_USERNAME2,
                                            password=PATIENT_PASSWORD2,
                                            email=PATIENT_EMAIL2)
        patient2 = Patient.objects.create(user=patient_user2,
                                          first_name=PATIENT_FIRST_NAME2,
                                          last_name=PATIENT_LAST_NAME2)
        patient2.save()

        patients = [patient, patient2]
        doctor.patients =  patients
        doctor = Doctor.objects.filter(user=doctor_user)
        self.assertEqual(len(doctor), 1)
        doctor = doctor[0]
        self.assertListEqual(list(doctor.patients.all()), patients)
        self.assertEqual(len(patient.doctors.all()), 1)
        self.assertEqual(patient.doctors.all()[0], doctor)
        self.assertEqual(len(patient2.doctors.all()), 1)
        self.assertEqual(patient2.doctors.all()[0], doctor)