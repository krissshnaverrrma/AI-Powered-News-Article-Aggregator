import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from news.models import Article
from news.utils import fetch_and_summarize


class Command(BaseCommand):
    help = "Scrapes AI news from Analytics India Magazine"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            "Accessing Indian AI news feed..."))
        url = "https://analyticsindiamag.com/category/ai-news/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.select('h3.entry-title a')[:10]

        for item in headlines:
            title = item.text.strip()
            link = item['href']

            if not Article.objects.filter(link=link).exists():
                try:
                    fetch_and_summarize(title, link)
                    self.stdout.write(
                        self.style.SUCCESS(f"Processed: {title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error: {e}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped: {title}"))
