from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def root(request):
    name = request.GET.get('name', 'guest')
    response = 'Hi, {}'.format(name)
    return HttpResponse(response)


def hello(request, name):
    response = 'Hi, {}'.format(name)
    return HttpResponse(response)


def square(request, number):
    number = number ** 2
    response = 'number ^ 2 = {}'.format(number)
    return HttpResponse(response)


def sequence(request, number1, number2):
    step = -1 if number1 > number2 else 1
    number_list = range(number1, number2 + step, step)
    return render(request, 'sequence.html', {'number_list': number_list})
