from django.conf.urls import include, url
from django.contrib import admin
from core.views import index
from django.conf import settings

if settings.DEBUG:
    urlpatterns = [
        url(r'^$', index),
    ]
else:
    urlpatterns = []

urlpatterns += [
    url(r'^admin/', include(admin.site.urls))
]
