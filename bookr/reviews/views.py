from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from reviews.models import Book
from .utils import average_rating


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


def welcome_view(request):
    # message = f'<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>'
    # return HttpResponse(message)
    return render(request, 'reviews/home_page.html')


class HomePageView(TemplateView):
    template_name = 'reviews/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.count()
        return context


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})

    context = {
        'book_list': book_list
    }
    return render(request, 'reviews/book_list.html', context)