from django.test import TestCase
from django.urls import reverse
from .models import List


class TodoCrudTests(TestCase):
    def test_create(self):
        resp = self.client.post(reverse('home'), {'item': 'Buy milk'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(List.objects.filter(item='Buy milk', completed=False).exists())
        self.assertContains(resp, 'Buy milk')

    def test_read_pages(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertContains(self.client.get(reverse('about')), 'Bob')

    def test_strike_and_unstrike(self):
        it = List.objects.create(item='Task')
        self.client.get(reverse('strike', args=[it.id]))
        it.refresh_from_db()
        self.assertTrue(it.completed)
        self.assertContains(self.client.get(reverse('home')), '<s>Task</s>')
        self.client.get(reverse('unstrike', args=[it.id]))
        it.refresh_from_db()
        self.assertFalse(it.completed)

    def test_delete(self):
        it = List.objects.create(item='Temp')
        resp = self.client.get(reverse('delete', args=[it.id]))
        self.assertRedirects(resp, reverse('home'))
        self.assertFalse(List.objects.exists())
