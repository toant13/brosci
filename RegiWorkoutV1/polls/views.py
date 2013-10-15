# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at question %s." % poll_id)

def results(request, poll_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on question %s." % poll_id)