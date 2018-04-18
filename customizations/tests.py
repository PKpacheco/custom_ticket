# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from mock import (
    MagicMock,
    patch,
)
from django.contrib.auth import get_user_model
from social_django.models import UserSocialAuth
from django.test import TestCase, RequestFactory
from .views import create_webhook, get_token
from django.contrib.auth.models import AnonymousUser, User
from .forms import FormCustomization
from customizations.utils import get_unique_file_name
from freezegun import freeze_time



class TestFormCustomization(TestCase):
    def test_form(self):
        form_data = {'name': 'testform', 'select_event': 'apply_all', 'logo': None, 'message': 'Test', 'select_design_template': 'design_one', 'message_ticket': 'Test'}
        form = FormCustomization(form_data)
        self.assertTrue(form.is_valid)


class TestCustomizationsWithNoWebhook(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='edacticket',
            password='12345',
            email='edacticket@gmail.com',
            first_name='edacticket',
            is_active=True,
        )
        self.factory = RequestFactory()
        self.auth = UserSocialAuth.objects.create(
            user=self.user, provider='eventbrite', uid="249759038146", extra_data={'access_token': 'HJDTUHYQ3ZVTVLMN52VZ'})

    # @patch(
    #     )
    # def test_post(self):

    @patch(
        'customizations.views.Eventbrite.post',
        return_value={
            u'user_id': u'249759038146',
            u'created': u'2018-04-13T07:19:38Z',
            u'event_id': None,
            u'resource_uri': u'https://www.eventbriteapi.com/v3/webhooks/646089/',
            u'endpoint_url': u'https://custom-ticket-heroku.herokuapp.com/mail/mail/',
            u'actions': [u'order.placed'],
            u'id': u'646089'
        }
    )
    def test_create_webhook(self, mock_requests):
        token = 'HJDTUHYQ3ZVTVLMN52VZ'
        id_webhook = create_webhook(token)

        self.assertEquals(id_webhook, '646089')
        mock_requests.assert_called_once()
        self.assertEquals(
            mock_requests.call_args_list[0][0][0],
            u'/webhooks/',
        )

    def test_get_token(self):
        request = self.factory.post('/customizations/create-customization/')
        request.user = self.user
        token = get_token(request)
        self.assertEquals(token, 'HJDTUHYQ3ZVTVLMN52VZ')


    @freeze_time("2012-01-14 03:21:34")
    def test_get_unique_file_name(self):

        request = self.factory.post('/customizations/create-customization/')
        request.user = self.user
        unique_name = get_unique_file_name(request, 'nombre del archivo.png')
        self.assertEquals(
            unique_name,
            'edacticket-3-e4122a5c7387fc823e534bdfa600f176cef7cb27732f90323cba4b29-nombre-del-archivo.png'
        )
