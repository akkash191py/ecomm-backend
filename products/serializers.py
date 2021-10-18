from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'       # all Product models data

        #exclude = ['id']        # exclude the id  and show all data.
