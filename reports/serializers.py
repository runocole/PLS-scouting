from rest_framework import serializers
from .models import Report, Team
from teams.serializers import TeamSerializer

class ReportSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    team_logo = serializers.SerializerMethodField()
    team_color = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(source='team', write_only=True, queryset=Team.objects.all())

    class Meta:
        model = Report
        fields = [
            'id', 'team', 'team_id', 'team_name', 'team_logo', 'team_color',
            'author', 'author_name', 'status', 'key_players', 'match_stats',
            'tactical_summary', 'performance_insights', 'created_at', 'updated_at'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_team_name(self, obj):
        return obj.team.name if obj.team else None

    def get_team_logo(self, obj):
        return obj.team.logo.url if obj.team and obj.team.logo else None

    def get_team_color(self, obj):
        return obj.team.color if obj.team and obj.team.color else None
