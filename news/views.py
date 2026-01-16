from django.core.management import call_command
from django.shortcuts import redirect, render

from .models import Article


def home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'articles': articles})


def refresh_news(request):
    call_command('scrape_news')
    return redirect('home')
