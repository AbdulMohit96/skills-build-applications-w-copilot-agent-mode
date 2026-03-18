from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    description = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return f"{self.user.name} - {self.description}"

class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} ({self.user.name})"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name}: {self.points} points"
