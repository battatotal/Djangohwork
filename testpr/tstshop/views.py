import re

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django.shortcuts import render
from rest_framework.response import Response

from .models import Product, Image
from .serializers import ProductSerializer
import io

class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend ]
    filterset_fields = ['status']
    search_fields = ['title', 'art']

    def list(self, request, *args, **kwargs): #скопировал list из миксина
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        #if 'image' in serializer.data: #без этой проверки, при наличии товара без фото, выдает ошибку
        for d in serializer.data: #добавил цикл
            if len(d['image']) > 0:  # без этой проверки, при наличии товара без фото, выдает ошибку
                adr = re.search(r'/media/images/.*', d['image'][0]['path'])[0].split('.')[0]
                fmt = d['image'][0]['formats']
                d['image'][0]['path'] = adr

                if fmt in ['png', 'jpg', 'PNG', 'JPG']:
                    d['image'][0]['formats'] = [fmt] + ["webp"]
                else:
                    d['image'][0]['formats'] = [fmt]

        return Response(serializer.data)




class DetailView(generics.GenericAPIView):
    lookup_field = "title"
    queryset = Product.objects.all()
    def get(self, request, title):
        product = self.get_object()
        p = ProductSerializer(product).data

        if len(p['image']) > 0:
            adr = p['image'][0]['path'].split('.')[0]
            fmt = p['image'][0]['formats']
            p['image'][0]['path'] = adr
            # p['image'][0]['formats'] = [format] + ["webp"]
            if fmt in ['png', 'jpg', 'PNG', 'JPG']:
                p['image'][0]['formats'] = [fmt] + ["webp"]
            else:
                p['image'][0]['formats'] = [fmt]
        return Response(p)






