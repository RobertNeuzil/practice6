from django.shortcuts import render
from django.http import HttpResponse
from .models import ThingsToDo

def index(request):
	

	listofthings = ThingsToDo.objects.order_by('id')


	context = {'listofthings': listofthings}

	return render(request, 'home/index.html', context)
# Create your views here.
