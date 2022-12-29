from random import sample
import telebot
import decouple


def gerar_jogos(seed=1):
    numeros = []
    lista = []    
    for _ in range(1, seed + 1):    
        numeros = sorted(sample(range(1, 61), 6))
        lista.append(numeros)     
    lista_ordenada = sorted(lista, key=lambda x: x[0])   
    result = lista_ordenada[0]
    return '  '.join(str(i) for i in result)

CHAVE_API = decouple.config('CHAVE_API')
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['GerarJogo'])
def ver_escala(mensagem):
    text = gerar_jogos()
    bot.send_message(mensagem.chat.id, text)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    text = """
    Clique no link abaixo 

        /GerarJogo

    """
    bot.reply_to(mensagem, text)

bot.polling()