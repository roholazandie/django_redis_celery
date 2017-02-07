from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [url('^polls/', include('polls.urls')),
 url('^detail/', include('polls.urls')),
 url('^init_work/', include('polls.urls')),
 url('^admin/', admin.site.urls)]