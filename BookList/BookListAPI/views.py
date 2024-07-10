from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.

# @api_view(['GET', 'POST'])
# def books(request):
#     return Response('List of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')

        if (author):
            return Response({"message": "list of the books by " + author}, status.HTTP_200_OK)
        return Response({"message": "list of the books"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"title": request.data.get('title')}, status.HTTP_201_CREATED)
    
class Book(APIView):
    def get(self, request, pk):
        return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status.HTTP_200_OK)
    


# class MenuItemView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        
        # Debug print statement
        # print("Request Method:", request.method)
        # print("Request:", request)
        # print("Query Params:", request.query_params)
        
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        
        if category_name:
            items = items.filter(category__title=category_name)

        if to_price:
            items = items.filter(price__lte=to_price)

        if search:
            items = items.filter(title__contains=search)

        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    
    # elif request.method == 'POST':
    #     serialized_item = MenuItemSerializer(data=request.data)
    #     serialized_item.is_valid(raise_exception=True)
    #     serialized_item.save()
    #     return Response(serialized_item.validated_data, status=status.HTTP_201_CREATED)

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']


@api_view()
@permission_classes([IsAuthenticated])
def secretMessage(request):
    return Response({"message": "Some secret message"})