from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
admin.autodiscover()

# importing the home function from index.py in TasksManager > views > index.py
# need to do this because strings are not allowed any longer in urlpatterns
from TasksManager.views.index import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # this path is looking for the index 
    path("", home, name="home"),
]