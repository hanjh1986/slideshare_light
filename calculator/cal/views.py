from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	"""signup to register users
	"""
	if request.method == 'POST':
		userform = UserCreationForm(request.POST)
		if userform.is_valid():
			userform.save()

			return HttpResponseRedirect(reverse("signup_ok"))

	elif request.method == 'GET':
		userform = UserCreationForm()

	return render(request, "signup.html", {"userform":userform,})


def calculate(request):
	result=''
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		number1 = int(request.POST['number1'])
		number2 = int(request.POST['number2'])
		operation = request.POST['operation']

		if operation == 'plus':
			result = number1 + number2
		elif operation == 'minus':
			result = number1 - number2
		elif operation == 'multiply':
			result = number1 * number2
		elif operation =='divide':
			result = number1 / number2
		else:
			result = 'Nothing'

	return render(request, 'cal/calculate.html', {'result':result,})