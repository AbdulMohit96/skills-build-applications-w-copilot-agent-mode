from django.test import TestCase
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = UserProfile.objects.create(name='Test User', email='test@example.com', team=self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, description='Test Activity', duration=60)
        self.assertEqual(activity.description, 'Test Activity')

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team=self.team, points=50)
        self.assertEqual(leaderboard.points, 50)
