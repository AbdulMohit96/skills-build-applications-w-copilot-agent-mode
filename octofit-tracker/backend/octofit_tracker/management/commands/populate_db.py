from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.UserProfile.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create users (super heroes)
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': marvel},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user_obj = app_models.UserProfile.objects.create(name=u['name'], email=u['email'], team=u['team'])
            user_objs.append(user_obj)

        # Create activities
        for user in user_objs:
            for i in range(3):
                app_models.Activity.objects.create(user=user, description=f"Activity {i+1} for {user.name}", duration=30+i*10)

        # Create workouts
        for user in user_objs:
            for i in range(2):
                app_models.Workout.objects.create(user=user, name=f"Workout {i+1} for {user.name}", difficulty='Medium')

        # Create leaderboard
        for team in [marvel, dc]:
            app_models.Leaderboard.objects.create(team=team, points=100 if team.name == 'Team Marvel' else 80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
