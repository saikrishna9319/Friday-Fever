# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

posts = [
    {
        'author': 'Saikrishna',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 04, 2020'
    },
    {
        'author': 'Manju',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 05, 2020'
    },

]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})