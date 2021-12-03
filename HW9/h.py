import telebot
from khayyam import JalaliDatetime
from gtts import gTTS
import random 
import qrcode

bot = telebot.TeleBot('2118381206:AAG_bFi7kilhKYNpniYWfZ9g-vY-S0FheNc')

@bot.message_handler(commands=['start'])
def salam(message):
	bot.reply_to(message ,' سلام ' + (message.chat.first_name) + '   خوش آمدی به بات من 🥰')

@bot.message_handler(commands=['game'])
def game(massage):
    txt = bot.send_message(massage.chat.id, '   یک عدد رو بین (۱۰ تا۱۰۰ ) حدس بزن منم بهت راهنمایی میکنم .😍  \n  حالا زمان بازی کردنه')
    bot.register_next_step_handler(txt, fugame)
    
@bot.message_handler(commands=['age'])
def age(massage):
    txt= bot.send_message(massage.chat.id, 'تاریخ تولدت رو وارد کن 😃. مثل: 1379/5/29')
    bot.register_next_step_handler(txt, fuage)

@bot.message_handler(commands=['voice'])
def voice(message):
    txt = bot.send_message(message.chat.id, 'متن انگلیسی مورد نظرتو وارد کن 🔡')
    bot.register_next_step_handler(txt, fuvoice)

@bot.message_handler(commands=['max'])
def max_num(message):
    global list 
    list = []
    txt = bot.send_message(message.chat.id, 'اعداد را وارد کن.🔢    به عنوان مثال : 14,7,78')
    bot.register_next_step_handler(txt, calmax)

@bot.message_handler(commands=['argmax'])
def argmax_num(message):
    global list 
    list = []
    txt = bot.send_message(message.chat.id, 'اعداد را وارد کن.🔢    به عنوان مثال : 14,7,78')
    bot.register_next_step_handler(txt, argmax)

@bot.message_handler(commands=['qrcode'])
def qrcode_f(massage):
    txt = bot.send_message(massage.chat.id, 'لینک را وارد کن. مثال: https://github.com/samiramohammadian')
    bot.register_next_step_handler(txt, fuqrcode)

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, """""
/start
خوش آمد گویی

/game 
بازی حدس اعداد 

/age
تاریخ تولد را به هجری شمسی وارد میکنید و سن خود را دریافت خواهید کرد

/voice
با ارسال یک جمله انگلیسی صوت آن را دریافت خواهید کرد

/max
یک آرایه به صورت 14,7,78,15,8,19,20 وارد میکنید و بزرگترین مقدار را دریافت خواهید کرد

/argmax
یک آرایه به صورت 14,7,78,15,8,19,20 وارد میکنید و اندیس بزرگترین مقدار را دریافت خواهید کرد

/qrcode
یک متن وارد میکنید و بارکد آن را دریافت خواهید کرد

/help
راهنمای دستورات من را دریافت خواهید کرد

""")



RANDOM_NUMBER = int(random.random()*100)
def new_randomNumber():
    global RANDOM_NUMBER
    RANDOM_NUMBER=int(random.random()*100)

def fugame(m):
    global RANDOM_NUMBER
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('بازی جدید')
    markup.add(btn1)
    if not m.text.startswith("/"):
        try:
            if m.text=='بازی جدید':
                new_randomNumber()
                bot.send_message(m.chat.id, ':بازی جدید شروع شد💪. یک عدد جدید حدس بزن😍🙄', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                bot.register_next_step_handler_by_chat_id(m.chat.id, fugame)
            elif int(m.text)<RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'برو بالا⬆️', reply_markup=markup)
                bot.register_next_step_handler(msg, fugame)
            elif int(m.text)>RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'بیا پایین⬇️', reply_markup=markup)
                bot.register_next_step_handler(msg, fugame)
            elif int(m.text)==RANDOM_NUMBER:
                msg = bot.send_message(m.chat.id, 'برنده شدی✅ ', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except ValueError:
            bot.send_message(m.chat.id, 'لطفا عدد وارد کنید 🙄', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
        except:
            bot.send_message(m.chat.id, 'مشکلی پیش آمده. بعدا تلاش کنید 🙁', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')
        
        
def fuage(m):
    if not m.text.startswith('/'):
        userBirth = m.text.split('/')
        if len(userBirth)==3:
            difference = JalaliDatetime.now() - JalaliDatetime(userBirth[0], userBirth[1], userBirth[2])
            bot.send_message(m.chat.id, 'سن شما '+ str(difference.days//365))
        else:
            bot.reply_to(m, 'مشکلی در ورودی پیش امده 🥲.')
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')


def fuvoice(m):
    if not m.text.startswith('/'):
        try:
            vc = gTTS(text=m.text, slow=False)
            vc.save('voice.ogg')
            voice = open('voice.ogg', 'rb')
            bot.send_voice(m.chat.id, voice)
        except:
            bot.send_message(m.chat.id, 'مشکلی پیش آمده. بعدا تلاش کنید 🙁')
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')


def calmax(m):
    if not m.text.startswith('/'):
        try:
            message_text = m.text
            numbers = message_text.split(',')
            for num in numbers:
                list.append(int(num))
            maxnum = max(list)
            bot.reply_to(m, 'بزرگترین عدد آرایه :‌ ' +str(maxnum))
        except ValueError:
            bot.reply_to(m, 'این عدد نیست😶')
        except :
            bot.send_message(m.chat.id, 'مشکلی پیش امده بعدا تلاش کنید')
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')       


def argmax(m):
    if not m.text.startswith('/'):
        try:
            message_text = m.text
            numbers = message_text.split(',')
            for num in numbers:
                list.append(int(num))
            maxnum = max(list)
            max_index = list.index(maxnum)
            bot.reply_to(m, ' بزرگتربن عدد در خانه اندیس ' +str(max_index))

        except ValueError:
            bot.reply_to(m, 'این عدد نیست😶')
        except :
            bot.send_message(m.chat.id, 'مشکلی پیش امده بعدا تلاش کنید')
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')       


def fuqrcode(m):
    if not m.text.startswith('/'):
        try:
            img = qrcode.make(m.text)
            img.save('QRCODE.png')
            photo = open('QRCODE.png', 'rb')
            bot.send_photo(m.chat.id, photo)
        except:
            bot.send_message(m.chat.id, ' مشکلی پیش امده بعدا تلاش کنید')
    else:
        bot.reply_to(m, 'تو یک کامند وارد کردی . 🤔')
   

bot.polling(none_stop=True)