from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    username = models.CharField(max_length=100)
    discord_id = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Sprint(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Commitment(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    commitment_description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class VoiceChannelLog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=100)
    joined_at = models.DateTimeField()
    left_at = models.DateTimeField(null=True, blank=True)

class Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    answer_text = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)

class Checklist(models.Model):
    commitment = models.ForeignKey(Commitment, on_delete=models.CASCADE)
    check_date = models.DateField()
    status = models.BooleanField(default=False)