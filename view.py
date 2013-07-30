from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world website with python")