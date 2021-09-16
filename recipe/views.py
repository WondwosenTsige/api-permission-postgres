from rest_framework import generics
from .serializer import RecipeSerializer 
from .models import Recipe
from .permissions import IsOwnerOrReadOnly

class RecipeList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer