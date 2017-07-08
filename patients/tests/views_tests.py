from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import json
from rest_framework.test import APIClient


class PatientsViewsTest(TestCase):

    fixtures = ['patients_testdata', 'patients_testdata_users']

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        self.logout()

    def login(self, username):
        user = User.objects.get(username=username)
        self.client.force_authenticate(user=user)

    def logout(self):
        self.client.force_authenticate(user=None)

    def test_create_account(self):
        """
        You should be able to create an account without logging in
        """
        response = self.client.post('/patients/',
                                    json.dumps({"username": 'patient_user1',
                                                "password": 'patient_pass1',
                                                "email": 'eamil@email.com',
                                                "first_name": 'Fred',
                                                "last_name": 'Johnson'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_account(self):
        """
        You should only be able to see your own account after logging in
        """
        response = self.client.get('/patients/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login('mddrill')

        response = self.client.get('/patients/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/patients/2/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_accounts_list(self):
        """
        You should be able to see the list of accounts without logging in
        """
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_account(self):
        """
        You should only be able to edit your own account
        """
        response = self.client.patch('/patients/1/',
                                     json.dumps({"email": "newemail@email.com"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login('mddrill')

        response = self.client.patch('/patients/1/',
                                     json.dumps({"email": "newemail@email.com"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch('/patients/2/',
                                     json.dumps({"email": "newemail@email.com"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_account(self):
        """
        You should only be able to delete your own account
        """
        response = self.client.delete('/patients/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.login('mddrill')

        response = self.client.delete('/patients/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/patients/2/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)