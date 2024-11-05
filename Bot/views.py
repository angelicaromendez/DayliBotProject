from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from models import Bot
from serializers import BotSerializer


# Create your views here.

class CreateBotView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = BotSerializer(data=data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()

        return Response ({'message': 'Bot created successfully'}, status= status.HTTP_201_CREATED)

class RetrieveBotView(APIView):
    
    def get(self, request, bot_id):
        bots_obj = get_object_or_404(Bot, id=bot_id)
        serializer = BotSerializer(bots_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateBotView(APIView):
    
    def put(self, request, bot_id):
        data = request.data
        bots_obj = get_object_or_404(Bot, id=bot_id)
        serializer = BotSerializer(instance=bots_obj, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Bot updated successfully'}, status=status.HTTP_200_OK)