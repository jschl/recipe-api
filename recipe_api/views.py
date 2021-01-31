from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer

@api_view(['GET'])
def filter_recipe(request, *args, **kwargs):
    ingredient = kwargs['ingredient']
    queryset = Recipe.objects.all().filter(ingredients__icontains=ingredient)
    serializer_class = RecipeSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)
