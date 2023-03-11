from rest_framework import generics
import requests
from django.http import JsonResponse

from .models import Jokes
from .serializers import JokeSerializer


class JokeList(generics.ListCreateAPIView):
    serializer_class = JokeSerializer

    def get_queryset(self):
        queryset = Jokes.objects.all()
        return queryset


class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokeSerializer


class JokeChuck(generics.ListCreateAPIView):
    serializer_class = JokeSerializer

    def get_queryset(self):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        text = response.json()['value']
        save_joke = Jokes.objects.create(joke=text)
        return JsonResponse({"joke": text})