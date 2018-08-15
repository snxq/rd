from django.test import TestCase
from RESTfulAPI.models import Picture, Tag
# Create your tests here.


class TestSearch(TestCase):
    def setUp(self):
        self.pics = [
            {
                "name": "测试1",
                "source": "https://test.com",
                "tags": ["测试", "1"]
            },
            {
                "name": "test1",
                "source": "https://test2.com",
                "tags": ["test", "1"]
            }
        ]
        for pic in self.pics:
            obj = Picture.objects.create(name=pic['name'], source=pic['source'])
            obj.tags.set(
                Tag.objects.get_or_create(name=tag)[0]
                for tag in pic['tags']
            )

        self.api = '/api/v1/search/'

    def test_get_base(self):
        response = self.client.get(f"{self.api}?keyword=测试")
        self.assertEqual(response.json()[0], self.pics[0])
