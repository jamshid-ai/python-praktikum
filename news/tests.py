from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='tema', text='lorem ipsum doler dots')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'tema')
        self.assertEqual(expected_object_text, 'lorem ipsum doler dots')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='tema 2', text='lorem ipsum doler dotss')

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'news/index.html')
