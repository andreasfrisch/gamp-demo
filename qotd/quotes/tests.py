from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from quotes.models import Quote

def create_quote(category, date, content):
    return Quote.objects.create(
                category = category,
                published_date = date,
                content = content,
            )

class QuoteNewestViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('quotes:newest'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No quote available')
        self.assertEqual(response.context['quote'], None)

    def test_questions_exist(self):
        """
        If multiple questions exist, return only the latest
        """
        create_quote("test", timezone.now(), "This is now")
        create_quote("test", timezone.now() - timedelta(days=2), "This was then")
        response = self.client.get(reverse('quotes:newest'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is now")


class QuoteIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, show nothing
        """
        response = self.client.get(reverse('quotes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['quotes'], [])

    def test_questions_exist(self):
        """
        If multiple questions exist, show all
        """
        create_quote("test", timezone.now(), "This is now")
        create_quote("test", timezone.now() - timedelta(days=2), "This was then")
        response = self.client.get(reverse('quotes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is now")
        self.assertContains(response, "This was then")

