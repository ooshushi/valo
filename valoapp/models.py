from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Agent(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Map(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Weapon(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Player(BaseModel):
    username = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

class MatchResult(BaseModel):
    map_played = models.ForeignKey(Map, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner')
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='loser')
    match_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.winner} vs {self.loser} on {self.map_played} ({self.match_date})"
