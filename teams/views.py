
from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
      try:
        serializer.save()
      except Exception as e:
        print("ERROR DURING TEAM CREATE:", e)
        raise


class TeamDetailView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

