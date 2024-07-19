from django.test import TestCase
from django.urls import reverse


class Homepagetests(TestCase):
    def test_homepagename(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepagecontent(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home page')

    def test_homepaggeurl(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepagetemplateuse(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
