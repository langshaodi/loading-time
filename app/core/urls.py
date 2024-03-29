from django.conf.urls import include, url
from django.contrib import admin
from core.views import index, urls_as_view
from games.views import GameView, DefaultGameView, MultiGameView
from responses.views import ResponseView

urlpatterns = []

apipatterns = [
    url(r'^game/$', GameView.as_view()),
    url(r'^game/default/$', DefaultGameView.as_view()),
    url(r'^game/multi/$', MultiGameView.as_view()),
    url(r'^response/$', ResponseView.as_view())
]

urlpatterns += [url(r'^api/', include(apipatterns))]

urlpatterns += [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/$', urls_as_view)
]
