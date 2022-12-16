import json
from rest_framework import serializers, response
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ("path","formats")


class ProductSerializer(serializers.ModelSerializer):

    image = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title', 'art', 'status', 'image')

        depth = 1

