# todo/todo_api/models.py
import uuid

from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default=uuid.uuid4)
    deckname = models.CharField(max_length = 180)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add = True,null=True)

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
    
