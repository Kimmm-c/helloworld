from django.urls import path
from .views import homePageView, aboutPageView, kimPageView, results, homePost


urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('kim/', kimPageView, name='kim'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
