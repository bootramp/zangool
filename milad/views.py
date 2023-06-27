from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def milad(request):
    return HttpResponse('''<a href="https://varzesh3.com">milad</a>''')