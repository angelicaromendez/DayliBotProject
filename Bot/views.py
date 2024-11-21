from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bot
from Bot.serializers import BotSerializer


# Create your views here.

class CreateBotView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = BotSerializer(data=data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()
        return Response ({'message': 'Respuesta guardada exitosamente'}, status= status.HTTP_201_CREATED)

class RetrieveBotView(APIView):
    
    def get(self, bot_id):
        bot_obj = get_object_or_404(Bot, id=bot_id)
        serializer = BotSerializer(bot_obj)
        return Response(serializer.data)
    
    def put(self, request, bot_id):
        bot_obj = get_object_or_404(Bot, id=bot_id)
        serializer = BotSerializer(instance=bot_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, bot_id):
        bot_obj = get_object_or_404(Bot, id=bot_id)
        bot_obj.status = False
        bot_obj.save()
        return Response({'message': 'Información eliminada correctamente'}, status=status.HTTP_200_OK)