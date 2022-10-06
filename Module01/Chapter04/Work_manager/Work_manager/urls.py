from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
admin.autodiscover()

# importing the home function from index.py in TasksManager > views > index.py
# need to do this because strings are not allowed any longer in urlpatterns
from TasksManager.views.index import page
from TasksManager.views.index_for_templates import public_index
from TasksManager.views.connection import connections

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_index, name="public_index"),
    path('connection', connections, name="public_connection")
    
    # deprecated url(r'^index$', 'TasksManager.views.index.page', name="public_index"),
    # debrecated url(r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
]