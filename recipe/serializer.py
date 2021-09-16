from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        #Include all the fields
        fields = "__all__"
        model = Recipe