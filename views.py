from django.shortcuts import render

# Create your views here.

print('ON EST DANS VIEWS.PY')
def index( request, *args, **kwargs):
    print('ON EST DANS LA VIEW INDEX')

    return render(request, 'book_discovery-session/index.html')
