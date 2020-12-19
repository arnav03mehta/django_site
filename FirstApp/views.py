from django.shortcuts import render
# from django.http import HttpResponse

index_items = [
    {
        'title': 'Github profile',
        'url': 'https://github.com/arnav03mehta'
    }, {
        'title': 'JS Projects',
        'url': 'projects/'
    }, {
        'title': 'Random link',
        'url': 'https://arnav03mehta.github.io'
    }, {
        'title': 'Random link',
        'url': 'https://arnav03mehta.github.io'
    }
]
project_items = [
    {
        'title': 'Github profile',
        'url': 'https://github.com/arnav03mehta'
    }, {
        'title': 'JS Projects',
        'url': 'projects/'
    }, {
        'title': 'Random link',
        'url': 'https://arnav03mehta.github.io'
    }, {
        'title': 'Random link',
        'url': 'https://arnav03mehta.github.io'
    }
]


def index(request):
    context = {
        'items': index_items,
        'page_head': ' Index Page ',
        'page_title': 'Main'
    }
    return render(request, 'index.html', context=context)


def projects(request):
    return render(request, 'projects.html')


def calculator_project(request):
    return render(request, 'jsProjects/calculator.html')
