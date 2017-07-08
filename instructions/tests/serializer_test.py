from django.test import TestCase
from instructions.models import Instruction
from instructions.serializers import InstructionSerializer
from doctors.models import Doctor
from patients.models import Patient

class InstructionsSerializerTest(TestCase):

    fixtures = ['instructions_testdata',
                'instructions_testdata_doctors',
                'instructions_testdata_patients',
                'instructions_testdata_users']

    def test_serializer(self):
        test_doctor_id = 2
        test_patient_id = 1
        test_instruction = 'Eat 43 cups of spinach every 15 minutes'
        instruction = Instruction.objects.create(doctor=Doctor.objects.filter(id=test_doctor_id)[0],
                                                 patient=Patient.objects.filter(id=test_patient_id)[0],
                                                 text=test_instruction)
        expected_json = \
            '{{"doctor": "{0}", "patient": "{1}", "text": "{2}"}}' \
                .format(test_doctor_id, test_patient_id, test_instruction)

        actual_json = InstructionSerializer.serialize(instruction)
        self.assertEqual(expected_json, actual_json)