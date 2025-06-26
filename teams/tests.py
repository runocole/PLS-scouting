from django.test import TestCase
from .models import Team

class TeamModelTest(TestCase):
    def setUp(self):
        self.league = League.objects.create(name="Premier League")
        self.team = Team.objects.create(
            name="Manchester United",
            logo="http://logo.com/mu.png",
            color="#FF0000",
            
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Manchester United")
        self.assertEqual(self.team.league.name, "Premier League")