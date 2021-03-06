from django.urls import path
from landing_page.views import scrape, render_landing_page , details_view , details_redirect
urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', render_landing_page, name="home"),
  path(r'^/details/(?P<object_id>[0-9]+)/$', details_view, name="details"),
  path("details/", details_redirect, name="details_redirect"),

]