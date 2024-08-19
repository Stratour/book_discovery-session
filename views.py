from django.shortcuts import render

# Create your views here.
def index( request, *args, **kwargs):

    return render(request, 'book_discovery_session/index.html')
