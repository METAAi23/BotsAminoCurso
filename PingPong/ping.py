from BotAmino import BotAmino #Importamos BotAmino para funcionar el bot.

client = BotAmino(Caterine Treise
@CaterineTreise76) #Definimos client como forma de usar BotAmino
client.prefix = "!" #Asignamos un prefix a nuestro bot.

#Creacion del Comando Ping que recibe un Pong.
@client.command(Caterine Treise
@CaterineTreise76)
def ping(data):
    data.subClient.send_message(data.chatId, message="Pong!")

print("Bot Iniciado") #La consola imprime esto cuando termina de cargar el bot.
client.launch() #Necesario para el funcionamiento del Bot.
