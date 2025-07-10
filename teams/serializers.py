from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)

    class Meta:
        model = Team
        fields = '__all__'
