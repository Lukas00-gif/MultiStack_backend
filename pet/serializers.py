from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Pet

#serializar um modelo
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'nome', 'historia', 'foto')