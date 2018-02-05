from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	context_dict = {'boldmessage':"wtf you doin here BOY"}
	return render(request, 'rango/index.html', context=context_dict)