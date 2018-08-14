from django.test import TestCase
from RESTfulAPI.models import Picture
# Create your tests here.


class TestSearch(TestCase):
    def setUp(self):
        self.pics = [
            {
                "name": "测试1",
                "source": "https://test.com"
            },
            {
                "name": "test1",
                "source": "https://test2.com"
            }
        ]
        for pic in self.pics:
            Picture.objects.create(**pic)
        self.api = '/api/v1/search/'

    def test_base(self):
        response = self.client.get(f"{self.api}?keyword=测试")
        self.assertEqual(response.json()[0], self.pics[0])