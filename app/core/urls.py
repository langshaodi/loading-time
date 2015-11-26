from django.conf.urls import include, url
from django.contrib import admin
from core.views import index, urls_as_view
from django.conf import settings
from games.views import GameView, DefaultGameView
from responses.views import ResponseView


if settings.DEBUG:
    urlpatterns = [
        url(r'^$', index),
    ]
else:
    urlpatterns = []

apipatterns = [
    url(r'^game/$', GameView.as_view()),
    url(r'^game/default/$', DefaultGameView.as_view()),
    url(r'^response/$', ResponseView.as_view())
]

urlpatterns += [url(r'^api/', include(apipatterns))]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/$', urls_as_view)
]
