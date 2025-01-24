from django.shortcuts import render
#from django.http import HttpResponse

# adding dummy data temproarily

posts=[
    {
        'author': 'bro',
        'title' : 'bullshit',
        'content' : 'first shit content',
        'date_posted' : 'February 10, 2025'
    },
    {
        'author': 'sis',
        'title' : 'cowshit',
        'content' : 'second shit content',
        'date_posted' : 'April 06, 2025'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')