from BotAmino import BotAmino #Importamos BotAmino para funcionar el bot.

client = BotAmino() #Definimos client como forma de usar BotAmino
client.prefix = "!" #Asignamos un prefix a nuestro bot.

#Creacion del Comando Ping que recibe un Pong.
@client.command()
def ping(data):
    data.subClient.send_message(data.chatId, message="Pong!")

print("Bot Iniciado") #La consola imprime esto cuando termina de cargar el bot.
client.launch() #Necesario para el funcionamiento del Bot.
