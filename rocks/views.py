from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rock
from .serializers import RockSerializer
import random

# Returns all rocks
class RockListView(generics.ListAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer

# Returns a single rock by ID
class RockDetailView(generics.RetrieveAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer

# Returns a random rock
class RockOfTheDayView(APIView):
    def get(self, request):
        rocks = Rock.objects.all()
        if not rocks:
            return Response({"message": "No rocks found"}, status=404)
        rock = random.choice(list(rocks))
        serializer = RockSerializer(rock)
        return Response(serializer.data)
