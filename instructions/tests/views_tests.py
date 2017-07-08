from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import json
from rest_framework.test import APIClient


class DoctorsViewsTest(TestCase):

    fixtures = ['instructions_testdata',
                'instructions_testdata_doctors',
                'instructions_testdata_patients',
                'instructions_testdata_users']

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        self.logout()

    def login(self, username):
        user = User.objects.get(username=username)
        self.client.force_authenticate(user=user)

    def logout(self):
        self.client.force_authenticate(user=None)

    def test_create_instruction(self):
        """
        Only doctors should be able to create instructions
        """
        response = self.client.post('/instructions/',
                                    json.dumps({"doctor": 1,
                                                "patient": 1,
                                                "text": "Chillax"}),
                                    content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

        self.login('lbullard')

        response = self.client.post('/instructions/',
                                    json.dumps({"doctor": 1,
                                                "patient": 1,
                                                "text": "Chillax"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.logout()
        self.login('mddrill')

        response = self.client.post('/instructions/',
                                    json.dumps({"doctor": 1,
                                                "patient": 1,
                                                "text": "Chillax"}),
                                    content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_account(self):
        """
        Doctors and patients should only be able to see their own instructions and only after logging in
        """
        response = self.client.get('/instructions/1/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        self.login('lbullard')

        response = self.client.get('/instructions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/instructions/2/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        self.logout()
        self.login('mddrill')

        response = self.client.get('/instructions/1/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/instructions/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_accounts_list(self):
        """
        No one should be able to see the list of all instructions
        """
        self.login('lbullard')
        response = self.client.get('/instructions/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        self.logout()
        self.login('mddrill')
        response = self.client.get('/instructions/')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_account(self):
        """
        Only doctors should be able to edit instructions, and only their own instructions
        """
        response = self.client.patch('/instructions/1/',
                                     json.dumps({"text": "new instruction"}),
                                     content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        self.login('lbullard')

        response = self.client.patch('/instructions/1/',
                                     json.dumps({"text": "new instruction"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch('/instructions/2/',
                                     json.dumps({"text": "new instruction"}),
                                     content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

        self.logout()
        self.login('mddrill')

        response = self.client.patch('/instructions/2/',
                                     json.dumps({"text": "new instruction"}),
                                     content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        """
        Doctors and patients should only be able to delete their own instructions and only after logging in
        """
        response = self.client.delete('/instructions/1/')
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.login('lbullard')

        response = self.client.delete('/instructions/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/instructions/2/')
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.logout()
        self.login('mddrill')

        response = self.client.delete('/instructions/1/')
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/instructions/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)