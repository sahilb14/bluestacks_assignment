from django.urls import path
from landing_page.views import scrape, render_landing_page
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', render_landing_page, name="home"),
]