from rest_framework import serializers
from .models import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [ 'deckname', 'description']

class FullDeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('deckname', 'description', 'uid')