from django.contrib.staticfiles import views


def index(request):
    return views.serve(request, 'index.html')
