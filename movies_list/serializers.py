from .models import Collections
from rest_framework import serializers

class CollectionsSerializers(serializers.ModelSerializer):


    class Meta:
        model = Collections
        fields = ['id', 'title', 'description', 'movies']
