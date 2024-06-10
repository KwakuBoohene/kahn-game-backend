# todo/todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    uid = models.CharField(max_length = 180)
    deckname = models.CharField(max_length = 180)

    def __str__(self):
        return self.deckname
    

class Card(models.Model):
    first_word = models.CharField(max_length = 180)
    second_word = models.CharField(max_length = 180)
    third_word = models.CharField(max_length = 180,null = True)
    fourth_word = models.CharField(max_length = 180,null = True)
    main_word = models.CharField(max_length = 180)
    deck = models.ManyToManyField(Deck)

    def __str__(self):
        return self.main_word
    
