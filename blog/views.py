from django.shortcuts import render

def index(requrest):
    return render(requrest, 'blog/index.html')
