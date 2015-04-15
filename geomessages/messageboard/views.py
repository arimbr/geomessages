from django.shortcuts import render, HttpResponse


# Create your views here.
def message_list(request):
    return HttpResponse(content="Hello World")
