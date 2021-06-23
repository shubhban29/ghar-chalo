from django.shortcuts import render
from rest_framework import status, permissions
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import *
import time
from datetime import date
from rest_framework import generics, mixins
from rest_framework import filters
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from .serializers import *
# Create your views here.
def index(request):
    return HttpResponse('This is just the deployed API. It does not have any user interface. To check API please go to this link <br><a href="https://app.swaggerhub.com/apis-docs/shubhban29/C3-pizza/1.0.0">API interface</a>')


class ResourceAPIView(APIView):
    permission_classes = [AllowAny]
    model = Pizza
    resource_serializer = PizzaSerializer
    matching_condition = 'CREATE'

    def get(self, request, pk):
        try:
            resource_item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.resource_serializer(resource_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            resource_item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.resource_serializer(resource_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
            serializer = self.resource_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            resource_item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({'message': 'The resource does not exist'},status=status.HTTP_404_NOT_FOUND)
        resource_item.delete()
        return Response({'message': 'The resource is deleted successfully!'})

class SetPagination(PageNumberPagination):

    page_size = 50
    page_size_query_param = 'count'

    def get_paginated_response(self, data):
        return Response(data, status=status.HTTP_200_OK)
class GetListView(generics.ListAPIView):
    model = Pizza
    resource_serializer = PizzaSerializer
    queryset = Pizza.objects.all()
    permission_classes = [AllowAny]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]
    filter_data = None
    Q1 = Q

    def get_queryset(self, page):
        """
        queryset of the Get
        """
        if page == 'all':
            queryset = self.model.objects.all()
            if self.filter_data:
                queryset = queryset.filter(**self.filter_data)
        else:
            m = int(page)
            if m == 0 or m == 1:
                queryset = self.model.objects.all()
                if self.filter_data:
                    queryset = queryset.filter(**self.filter_data)
                queryset = queryset[:50]
            else:
                n = (m-1)*50
                queryset = self.model.objects.all()
                if self.filter_data:
                    queryset = queryset.filter(**self.filter_data)
                queryset = queryset[n:n+50]
        return queryset

    def list(self, request, page, *args, **kwargs):
        self.search_term = None
        page_count = request.GET.get('page', None)
        dict1 = {}
        self._exclude = {}
        self._current_special_filter = {}
        for k, v in request.query_params.items():
            dict1[k] = v
        self.filter_data = dict1
        queryset = self.get_queryset(page)
        serializer = self.resource_serializer(queryset, many=True)
        if page == 'all':
            return Response(serializer.data, status=status.HTTP_200_OK)
        page_detail = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page_detail)