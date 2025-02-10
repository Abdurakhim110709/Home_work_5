from django.urls import path
from .views import DirectorListView, DirectorDetailView, MovieListView, MovieDetailView, ReviewListView, ReviewDetailView

urlpatterns = [
    path('/api/v1/directors/', DirectorListView.as_view(), name='director-list'),
    path('/api/v1/directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),
    path('/api/v1/movies/', MovieListView.as_view(), name='movie-list'),
    path('/api/v1/movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),
    path('/api/v1/reviews/', ReviewListView.as_view(), name='review-list'),
    path('/api/v1/reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]
