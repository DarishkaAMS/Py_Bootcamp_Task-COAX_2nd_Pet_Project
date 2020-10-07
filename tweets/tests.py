from django.test import TestCase
from .models import Tweet
from django.urls import reverse

# Create your tests here.
class TestHello(TestCase):

    def setUp(self):
        content = Tweet(content="Let me introduce Myself")
        content.save()
        # self.content.save() teardown

    def test_hello_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)