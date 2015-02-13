from django.shortcuts import render
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Create your views here.
def home(request, format=None):
  value = "hello world"

  return render(request, 'home.html', {'value' : value})


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer