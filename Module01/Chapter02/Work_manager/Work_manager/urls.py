from django.contrib import admin
from django.urls import path
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
]