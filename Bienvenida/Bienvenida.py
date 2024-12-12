from BotAmino import BotAmino

client = BotAmino(Caterine Treise
@CaterineTreise76)

@client.on_member_join_chat() #Bienvenida a un nuevo usuario, evento.
def bienvenida(data):
   #Usamos el modulo send_message para enviar el mensaje de bienvenida. Y el metodo mentionedUserIds para obtener la mencion del usuario.
   data.subClient.send_message(chatId=data.chatId, message=f"Eres bienvenido al Chat, <$@{data.author}$>", mentionUserIds=data.authorId)
   #Usamos data.author para tener el nickname del bienvenido y data.authorId para obtener la id del Usuario que se unio.

@client.on_member_leave_chat() #Hacemos una simple despedida de Chat.
def despedida(data):
    data.subClient.send_message(chatId=data.chatId, message="Esperamos verte muy pronto, cuidate en tu camino.")

print("Bot Iniciado")
client.launch()
