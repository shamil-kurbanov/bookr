from django.shortcuts import render, redirect


def index(request):
    context = {
        'name': request.GET.get('name') or 'world'
    }

    return render(request, 'reviews/base.html', context=context)


def book_search(request):
    search_text = request.GET.get('search', '')
    context = {
        'search_text': search_text,
    }
    return render(request, 'reviews/search-results.html', context=context)

# http://127.0.0.1:8000/book_search/?search=test

