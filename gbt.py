import requests
import telebot
from telebot import types
brok = telebot.TeleBot("5616976820:AAH6eXLoWEVvmbZFh07zsbWmNqIBk8RPomA")
ch = types.InlineKeyboardButton(text="عَبود؟",url="https://t.me/xx_YaBh")
hel = types.InlineKeyboardButton(text='فكرة البوت',callback_data='help')
@brok.message_handler(commands=["start"])
def start(message):
 bb = types.InlineKeyboardMarkup()
 bb.add(hel)
 brok.reply_to(message,'اهلاً بك في بوت البحث عن أكثر من 100 مليون رمز مفتوح المصدر يعيد إرساله مباشرة من رمز VS الخاص بك.',reply_markup=bb)
@brok.message_handler(func=lambda brok:True)
def ask(message):
  msg = message.text
  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Content-Type': 'application/json',
      'Origin': 'https://www.useblackbox.ai',
      'Alt-Used': 'www.useblackbox.ai',
      'Connection': 'keep-alive',
      'Referer': 'https://www.useblackbox.ai/home-codesearch',
  }

  json_data = {
      'userId': '',
      'textInput': f'{msg}',
      'source': 'webapp',
  }
  try:
  	url = requests.post('https://www.useblackbox.ai/autocompletev4', headers=headers, json=json_data)
  	aa = (url.json())
  	bb = aa['response']
  	b = types.InlineKeyboardMarkup()
  	b.add(ch)
  	brok.send_message(message.chat.id,bb,reply_markup=b)
  except:
  	brok.reply_to(message,'error')
  	
@brok.callback_query_handler(func=lambda call:True)
def help(call):
	brok.answer_callback_query(call.id, show_alert=True, text=f'''
	فكرة البوت انك تساله عن كود او تعطي كود فيه مشكلة او تطلب منه حل او تبحث عن كود 
	'''
)

print('run')
brok.infinity_polling()
