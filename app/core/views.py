from django.contrib.staticfiles import views
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
from django.conf import settings
import core.urls
import json


def recursively_build__url_dict(d, urlpatterns):
    for i in urlpatterns:
        if isinstance(i, RegexURLResolver):
            d[str(i.__dict__['_regex'])] = {}
            if str(i.__dict__['_regex']) != "^admin/":
                recursively_build__url_dict(
                    d[str(i.__dict__['_regex'])], i.url_patterns
                )
            else:
                d[str(i.__dict__['_regex'])] = "REDACTED"

        elif isinstance(i, RegexURLPattern):
                d[str(i.regex.pattern)] = i.callback.__name__


@api_view()
def urls_as_view(request):
    if settings.DEBUG:
        a = {}
        recursively_build__url_dict(a, core.urls.urlpatterns)
        return HttpResponse(
            json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')),
            content_type="application/json")
    else:
        return HttpResponse("")


def index(request):
    return views.serve(request, 'index.html')
