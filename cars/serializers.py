from rest_framework import serializers
from .models import Car

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "maker",
            "year",
            "admin",
        )
        model = Car