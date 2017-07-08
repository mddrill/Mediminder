from django.test import TestCase
from instructions.models import Instruction
from doctors.models import Doctor
from patients.models import Patient

class InstructionModelTest(TestCase):
    
    fixtures = ['instructions_testdata',
                'instructions_testdata_doctors',
                'instructions_testdata_patients',
                'instructions_testdata_users']

    def test_create_instruction(self):
        test_doctor_id = 2
        test_patient_id = 1
        test_instruction = 'Eat 43 cups of spinach every 15 minutes'
        instruction = Instruction.objects.create(doctor=Doctor.objects.filter(id=test_doctor_id)[0],
                                                 patient=Patient.objects.filter(id=test_patient_id)[0],
                                                 text=test_instruction)
        instruction.save()

        instruction = Instruction.objects.filter(doctor=test_doctor_id)
        self.assertEqual(len(instruction), 1)
        instruction = instruction[0]

        self.assertEqual(instruction.patient, test_patient_id)
        self.assertEqual(instruction.text, test_instruction)