from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    """" Serializer for Category Models """

    class Meta:
        model = Category
        fields = '__all__'            # all Category models field(data)




class QuantitySerializer(serializers.ModelSerializer):

    """ Serializer for Quantity Models """

    class Meta:
        model = QuantityVariant
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):

    """ Serializer for ColorVarient Models """

    class Meta:
        model = ColorVarient
        fields = '__all__'

# Creating  using ModelSerializer

class SizeSerializer(serializers.ModelSerializer):

    """ Serializer for SizeVarient Models """

    class Meta:
        model = SizeVarient
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):

    """Serializer for Product Model"""

    category  = CategorySerializer()              # serialize the category fields of Product Model
    quantity_type = QuantitySerializer()           # serialize the quantity_type fields of Product Model
    color_type = ColorSerializer()                  # serialize the color_type fields of Product Model
    size_type = SizeSerializer()                     # serialize the size_type fields of Product Model

    class Meta:
        model = Product
        fields = '__all__'       # all Product models field(data)

        #exclude = ['id']        # exclude the id  and show all data.


