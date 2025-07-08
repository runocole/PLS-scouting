from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_logo(self, obj):
        request = self.context.get('request')
        if obj.logo:
            logo_url = obj.logo.url
            if request:
                return request.build_absolute_uri(logo_url)
            return logo_url
        return None
