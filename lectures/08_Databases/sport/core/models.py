from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    kind = models.ForeignKey(Kind)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    num_games = models.IntegerField()
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


