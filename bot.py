import os
from decouple import config
import discord
from discord.ext import commands
from django.core.wsgi import get_wsgi_application
import logging

logging.basicConfig(level=logging.DEBUG)


# Obtener el token desde .env
TOKEN = config('DISCORD_BOT_TOKEN')

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DayliBot.settings')
application = get_wsgi_application()


# Configuración del bot de Discord
intents = discord.Intents.default()
intents.message_content = True  # Asegúrate de habilitar esto si necesitas contenido de mensajes

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hello(ctx):
    try:
        await ctx.send('¡Hola! Soy tu bot de Discord.')
    except Exception as e:
        print(f'Error en el comando hello: {e}')


@bot.command()
async def iniciar_sprint(ctx, duracion: int):
    # Guardar la duración del sprint en una base de datos o en un archivo
    await ctx.send(f'Sprint iniciado por {duracion} días.')

@bot.command()
async def finalizar_sprint(ctx):
    # Aquí puedes manejar la lógica para finalizar el sprint
    await ctx.send('Sprint finalizado.')

@bot.command()
async def agregar_equipo(ctx, *miembros: str):
    # Lógica para agregar miembros al equipo
    await ctx.send(f'Miembros del equipo añadidos: {", ".join(miembros)}.')

@bot.command()
async def hora_lanzamiento(ctx, hora: str):
    # Guardar la hora de lanzamiento
    await ctx.send(f'La hora de lanzamiento será a las {hora}.')

#@bot.event
#async def on_message(message):
 #   if message.author == bot.user:
  #      return
    # Aquí puedes manejar el almacenamiento de respuestas y hacer que sean visibles
   # await message.channel.send(f'{message.author}: {message.content}')
#preguntas = []

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Aquí puedes manejar cualquier lógica que necesites antes de procesar comandos

    # Procesar comandos después de manejar el mensaje
    await bot.process_commands(message)

@bot.command()
async def preguntar(ctx, pregunta: str):
    preguntas.append(pregunta)
    await ctx.send(f'Pregunta añadida: {pregunta}')

@bot.command()
async def resumen(ctx):
    resumen_preguntas = "\n".join(preguntas)
    await ctx.send(f'Resumen de preguntas:\n{resumen_preguntas}')

@bot.command()
async def recordatorio(ctx):
    # Aquí puedes manejar la lógica de recordatorio
    await ctx.send('¡Recuerda responder tus preguntas!')

compromisos = []

@bot.command()
async def agregar_compromiso(ctx, compromiso: str):
    compromisos.append(compromiso)
    await ctx.send(f'Compromiso añadido: {compromiso}')

@bot.command()
async def checklist(ctx):
    checklist_compromisos = "\n".join(compromisos)
    await ctx.send(f'Checklist de compromisos:\n{checklist_compromisos}')
respuestas = {}

@bot.command()
async def responder(ctx, respuesta: str):
    respuestas[ctx.author] = respuesta
    await ctx.send(f'{ctx.author} ha respondido: {respuesta}')

@bot.command()
async def control_respuestas(ctx):
    no_respuestas = [usuario for usuario in miembros_equipo if usuario not in respuestas]
    await ctx.send(f'Miembros que no han respondido: {", ".join(no_respuestas)}')
@bot.command()
async def recordatorio_cierre(ctx, dias: int):
    await ctx.send(f'Quedan {dias} días para el cierre del sprint.')
@bot.command()
async def configurar_equipo(ctx, canal: str, *miembros: str):
    # Lógica para configurar el canal y etiquetar a los usuarios
    await ctx.send(f'Equipo configurado en {canal} con miembros: {", ".join(miembros)}.')

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        await member.send(f'Has ingresado al canal de voz: {after.channel.name}')
    if before.channel is not None:
        await member.send(f'Has salido del canal de voz: {before.channel.name}')

@bot.command()
async def iniciar_dailies(ctx):
    await ctx.send('Las dailies han comenzado. Responde las siguientes preguntas:')
    await ctx.send('1. ¿Qué hiciste ayer?')
    await ctx.send('2. ¿Qué harás hoy?')
    await ctx.send('3. ¿Hay algo que te esté deteniendo en tu progreso?')
respuestas_dailies = {}

@bot.command()
async def responder_dailies(ctx, ayer: str, hoy: str, bloqueo: str):
    respuestas_dailies[ctx.author] = {
        'ayer': ayer,
        'hoy': hoy,
        'bloqueo': bloqueo
    }
    await ctx.send(f'Tus respuestas han sido registradas, {ctx.author}.')

@bot.command()
async def ver_respuestas(ctx):
    for usuario, respuestas in respuestas_dailies.items():
        await ctx.send(f'{usuario} - Ayer: {respuestas["ayer"]}, Hoy: {respuestas["hoy"]}, Bloqueo: {respuestas["bloqueo"]}')
compromisos_sprint = {}

@bot.command()
async def compromisos(ctx, *compromisos: str):
    compromisos_sprint[ctx.guild.name] = compromisos
    await ctx.send(f'Compromisos del equipo registrados: {", ".join(compromisos)}.')

@bot.command()
async def test(ctx):
    await ctx.send('El bot está funcionando.')



# Iniciar el bot
bot.run(TOKEN)


