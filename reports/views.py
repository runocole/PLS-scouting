from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer
from .permissions import IsAnalystOrReadOnly, IsReportOwnerOrReadOnly

class ReportListCreateView(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsAnalystOrReadOnly]

    def get_queryset(self):
        queryset = Report.objects.select_related('team', 'author').all()
        if self.request.user.role == 'analyst':
            queryset = queryset.filter(author=self.request.user)
        return queryset.order_by('-updated_at')

    def perform_create(self, serializer):
        # Prevent duplicate report for the same team by the same analyst
        team = serializer.validated_data.get('team')
        if Report.objects.filter(team=team, author=self.request.user).exists():
            raise serializers.ValidationError("You have already created a report for this team.")
        serializer.save(author=self.request.user)

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.select_related('team', 'author').all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsReportOwnerOrReadOnly]

class TeamReportsView(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Report.objects.filter(team_id=team_id).select_related('team', 'author')

class UpdateReportStatusView(generics.UpdateAPIView):
    queryset = Report.objects.select_related('team', 'author').all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsReportOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        report = self.get_object()
        status_value = request.data.get('status')
        if status_value:
            report.status = status_value
            report.save()
            return Response(ReportSerializer(report, context={'request': request}).data)
        return Response({'detail': 'Missing status'}, status=status.HTTP_400_BAD_REQUEST)
