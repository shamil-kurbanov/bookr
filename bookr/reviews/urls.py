from django.urls import path
from .views import HomePageView, welcome_view, book_list, book_detail

urlpatterns = [
    # path('', HomePageView.as_view(template_name='reviews/home_page.html'), name='home')
    path('', welcome_view, name='home_page'),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
]
