from rest_framework import serializers
from . models import *


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')

class StoreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('__all__')

class ProductCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('__all__')