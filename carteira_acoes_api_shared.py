# imports
import locale
import telebot
import requests

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# configs do Telelgram (TeleBot)
tg_id = [1,2,3] # ids Telegram de quem irá receber a mensagem no final (obter ids no bot @RawDataBot)
CHAVE_API="ID_DO_BOT_AQUI" # Criar um bot no Telegram através do Bot Father e preencha aqui a chave a chave. Ex: 5642342523:bATgMpYf-YGBD_8DEj4dXboZmvWkAY_A0jM
bot = telebot.TeleBot(CHAVE_API)

# Preencha a lista com as ações que deseja acompanhar
empresas = ['MXRF11','HCTR11','IRDM11','PETR4','MGLU3']

# Caminhos que o navegador deverá seguir, site e XPATH, necessário modificar caso haja alguma manutenção na página
url_base = 'https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/#empresa#/1'

txt = ''

for empresa in empresas:
    url = url_base.replace('#empresa#',empresa)
    response = requests.get(url)
    ret = response.json()
    txt += f'#{empresa.upper()}\n{locale.currency(ret[0]["vl_fechamento"])}\n\n'
    
txt = 'Atualização dos valores das ações\n\n' + txt
txt += '-------------------\n'
txt += 'Fonte: api-cotacao-b3.labdo.it\n'
txt += 'Desenvolvido por @walisilva' # favor não remover os créditos

for t in tg_id:
    bot.send_message(t, txt)
    print(f'Telegram: Enviado para [{str(t)}]')

