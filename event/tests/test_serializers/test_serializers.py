from django.test import TestCase
from event.serializers import EventSerializers
from event.tests.factories.users import UserFactory
from rest_framework.authtoken.models import Token
from django.test import Client

import json


class EventSerializersTestCase(TestCase):
    PASSWORD_USER = UserFactory.password

    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.get(user_id=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        self.val_dict = {'event_type': '2333', 'info': json.dumps({'work': '23'}), 'timestamp': '2011-09-01 13:20'}
        self.data_user = {'username': 'Bob', 'password': 'bob777'}

    def test_EventSerializers(self):
        serializer = EventSerializers(data=self.val_dict)
        self.assertEqual(serializer.is_valid(), True)

    def test_EventSerializers_create(self):
        response_post = self.client.post('/api/v1/event/', data=self.val_dict)
        response_get = self.client.get('/api/v1/event/')
        self.assertEqual(type(json.loads(response_post.content)), dict)
        self.assertEqual(type(json.loads(response_get.content)), list)
        self.assertEqual(len(json.loads(response_get.content)), 1)

    def test_UserSerializers(self):
        self.client = Client()
        response = self.client.post('/api/v1/registration/', data=self.data_user)
        self.assertEqual(json.loads(response.content)['id'], 2)
        self.assertEqual(json.loads(response.content)['username'], self.data_user['username'])