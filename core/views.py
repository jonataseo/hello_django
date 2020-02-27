from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse('Hello {}'.format(nome))

def soma(request, num1, num2):
    sum = num1 + num2
    return HttpResponse('O resultado da soma entre {} e {} é: {}'.format(num1, num2, sum))

def subtracao(request, num1, num2):
    subs = num1 - num2
    return HttpResponse('O resultado da subtracao entre {} e {} é: {}'.format(num1, num2, subs))

def multiplicacao(request, num1, num2):
    mult = num1 * num2
    return HttpResponse('O resultado da multiplicacao entre {} e {} é: {}'.format(num1, num2, mult))

def divisao(request, num1, num2):
    div = num1 / num2
    return HttpResponse('O resultado da multiplicacao entre {} e {} é: {}'.format(num1, num2, div))