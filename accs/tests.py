from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class Signupteset(TestCase):
    username = 'newusername'
    email = 'newemail@mail.com'
    def test_signupname(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signupurl(self):
        response = self.client.get('/accounts/signupp/')
        self.assertEqual(response.status_code, 200)

    def test_signupformmmmmmmm(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

