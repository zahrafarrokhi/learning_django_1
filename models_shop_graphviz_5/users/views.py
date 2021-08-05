from django.http import HttpResponse
# Create your views here.
def index(requset):
    return HttpResponse("hello")