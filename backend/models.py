# todo/todo_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task
    
class Card(models.Model):
    first_word = models.CharField(max_length = 180)
    second_word = models.CharField(max_length = 180)
    third_word = models.CharField(max_length = 180,null = True)
    fourth_word = models.CharField(max_length = 180,null = True)
    main_word = models.CharField(max_length = 180)

    def __str__(self):
        return self.task