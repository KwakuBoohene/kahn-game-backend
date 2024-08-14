from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Deck
from rest_framework.authtoken.models import Token
from .serializers import DeckSerializer,FullDeckSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def create(request):
    serializer = DeckSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Deck created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['GET'])
def read(request):
    if 'uuid' in request.query_params:
        deck = Deck.objects.filter(uid=request.query_params['uuid'])
    else:
        deck = Deck.objects.all()
    serializer = FullDeckSerializer(deck, many=True)
    return Response({'results': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request,deck_uid):
    uuid =deck_uid
    deck = get_object_or_404(Deck, uid=uuid)
    # update the deck
    if 'deckname' in request.data:
        deck.deckname = request.data['deckname']
    if 'description' in request.data:
        deck.description = request.data['description']
    deck.save()
    return Response({'message': 'Deck updated'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request):
    deck = get_object_or_404(Deck, uuid=request.data['uuid'])
    return Response(serializer.errors, status=status.HTTP_200_OK)

