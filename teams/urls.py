# teams/urls.py
from django.urls import path
from .views import TeamListCreateView, TeamDetailView

urlpatterns = [
    path('', TeamListCreateView.as_view(), name='team-list-create'),
    path('<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]
