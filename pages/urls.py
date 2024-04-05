from django.urls import path, include
from .views import aboutPageView, tryOut, makePrediction


urlpatterns = [
    path('', aboutPageView, name='about'),
    path('about/', aboutPageView, name='about'),
    path('tryOut/', tryOut, name='tryOut'),
    path('makePrediction/', makePrediction, name='makePrediction'),
    path('', include("django.contrib.auth.urls")),
]
