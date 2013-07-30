from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world website with python")

def Fuck_you(request):
	return HttpResponse("Test Fuck you")