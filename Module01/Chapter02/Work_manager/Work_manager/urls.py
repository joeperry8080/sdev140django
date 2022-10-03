#from django.conf.urls import include, url
from django.urls import include, re_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    re_path(r'^admin/', admin.site.urls),
]