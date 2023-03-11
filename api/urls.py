from django.urls import path
from .views import JokeList, JokeDetail, JokeChuck

urlpatterns = [
    path('joke/', JokeList.as_view()),
    path('joke/<int:pk>/', JokeDetail.as_view()),
    path('joke/random/', JokeChuck.as_view()),
]
