from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth.models import User


class SnackTestCase(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(
            name='Chips',
            purchaser=self.user,
            description='Delicious potato chips'
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_snack_list_view(self):
        url = reverse('snacks:snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertContains(response, self.snack.name)

    def test_snack_detail_view(self):
        url = reverse('snacks:snack_detail', args=[self.snack.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertContains(response, self.snack.name)
        self.assertContains(response, self.snack.description)
        self.assertContains(response, self.snack.purchaser.username)
