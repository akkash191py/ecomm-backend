from rest_framework import serializers
from .models import *

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'            # all Category models field(data)

# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


# Quantity Serializer
class QuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Quantity
        fields = '__all__'


# Color Serializer
class ColorSerializer(serializers.ModelSerializer):

    """ Serializer for ColorVarient Models """

    class Meta:
        model = Color
        fields = '__all__'


# Size Serializer
class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'



# Product Serializer
class ProductSerializer(serializers.ModelSerializer):

    category  = CategorySerializer()              # serialize the category fields of Product Model
    quantity_type = QuantitySerializer()           # serialize the quantity_type fields of Product Model
    color_type = ColorSerializer()                  # serialize the color_type fields of Product Model
    size_type = SizeSerializer()                     # serialize the size_type fields of Product Model

    class Meta:
        model = Product
        fields = '__all__'       # all Product models field(data)

        #exclude = ['id']        # exclude the id  and show all data.


# Product Serializer
class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'