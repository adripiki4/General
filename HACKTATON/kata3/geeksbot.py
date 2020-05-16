from telegram.ext import Updater
# token creado: 1178547533:AAHllEjbkfy35t5pAohjch7LNBbdFpG7VB0
def main():
    #Instaciamos el updater
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    #Añadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Añadiendo manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #Añadiendo manejador para el comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args = [2, 2]
    resultado = context.args[0] + int(context.args[1])
    resultado=str(resultado)
    update.message.reply_text("El resultado es " + resultado)


main()