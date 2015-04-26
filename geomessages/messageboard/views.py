from django.shortcuts import render, HttpResponse


# Create your views here.
def message_list(request):
    # Get access to URL query parameters
    # /api/v1/messages/?lat=66.434&lng=44.3453
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    content = "lat: {}, lng: {}".format(lat, lng)
    return HttpResponse(content=content)
