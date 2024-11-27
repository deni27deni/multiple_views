from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def deni(request):
    return HttpResponse('Deni is boy who loves Games and Anime')

def josh(request):
    return HttpResponse('<h1>Josh is a boy who loves Games</h1>')

def enosh(request):
    return HttpResponse('<h1><marquee>Enosh is boy who loves Anime</marquee></h1>')

def bioData(request):
    return HttpResponse('''
                            <h1>Name : Deni </h1>
                            <i>Age : 20</i><br><br>
                            <b>Gender : Male</b><br><br>
                            <img src='#'>
                        ''')
