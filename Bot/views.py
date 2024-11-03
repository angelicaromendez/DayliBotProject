from django.shortcuts import render

from rest_framework.views import APIView
from models import Bot
from serializers import BotSerializer


# Create your views here.

class CreateBotView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = BotSerializer(data=data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()