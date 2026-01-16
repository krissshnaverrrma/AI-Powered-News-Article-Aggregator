from django.contrib import admin
from django.urls import path

from news.views import home, refresh_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('refresh/', refresh_news, name='refresh_news'),
]
