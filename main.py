import telebot
import time
import random
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('7191661928:AAFRCRkvMSCRJbPcHmXRvMU3TtszLZtc69Y')

locations = [
    "Парк",
    "Зоопарк",
    "Караоке",
    "Готель",
    "Туалет",
    "Музей",
    "Художня галерея",
    "Театр",
    "Концертний зал",
    "Спортивний стадіон",
    "Парк розваг",
    "Водний парк",
    "Ботанічний сад",
    "Акваріум",
    "Історична пам'ятка",
    "Релігійна споруда",
    "Торговий центр",
    "Ринок",
    "Ресторан",
    "Кафе",
    "Бар",
    "Нічний клуб",
    "Бібліотека",
    "Школа"
]

messages = []

reg_started = True

again = False

game_ended = False

_registrations = []

random_location = ''

game_timer = None

spy_list = []
users = []
players2 = []
games = []

class User():
    def __init__(self,id,username,first_name):
        self.id = id
        self.username = username
        self.first_name = first_name

class Player(User):
    def __init__(self,id,username,first_name,role,location):
        super().__init__(id,username,first_name)
        self.role = role
        self.location = location

class Game():
    def __init__(self,status,reg_status):
        self.status = status
        self.messages = None
        self.reg_status = reg_status
        self.reg_list = None

    def get_messages(self):
        return self.messages

    def set_messages(self,msg):
        self.messages = msg

    def set_reg_list(self,reg_list):
        self.reg_list = reg_list

    def get_reg_list(self):
        return self.reg_list

    def set_reg_status(self,reg_status):
        self.reg_status = reg_status

    def get_reg_status(self):
        return self.reg_status

game1 = Game(status=True,reg_status=True)

def clearing():
    print('clear')
    global reg_started,players,messages,spy_list,game_ended,random_location,_registrations,again
    players = {}
    again = False
    messages = []
    spy_list = []
    game_ended = False
    random_location = ''
    reg_started = True
    _registrations = []

@bot.message_handler(commands=['start'])
def connect_the_game(message):
    if message.chat.type == 'private':
        if 'join_game' in message.text.lower():
            if message.from_user.id not in [player.id for player in players2] and not again:
                user_id = message.from_user.id
                username = message.from_user.username
                first_name = message.from_user.first_name

                users.append(User(user_id,username,first_name))

                join_game()

                bot.send_message(message.chat.id, "Ти в ігрі, друже!", reply_to_message_id=message.message_id)

            elif not again:
                bot.send_message(message.chat.id, "Ти вже в ігрі!", reply_to_message_id=message.message_id)

        else:
            bot.send_message(message.chat.id, f'Вітаю, {message.from_user.first_name}!')

@bot.message_handler(commands=['locations'])
def locations_list(message):
    bot.send_message(message.chat.id, '\n'.join(locations))

@bot.message_handler(commands=['game'])
def start_the_game(message):
    reply_markup = InlineKeyboardMarkup()

    join_button = InlineKeyboardButton("Приєднатися до гри", callback_data='join_game',
                                       url="https://t.me/newspygame_bot?start=join_game")
    reply_markup.add(join_button)

    msg1 = bot.send_message(
        message.chat.id,
        "Привіт! Я бот для гри Шпигун. Щоб приєднатися до гри, натисни кнопку нижче.",
        reply_markup=reply_markup
    )
    messages.append(msg1)

    game1.set_messages(msg1)

def join_game():
    if users:

        reply_markup = InlineKeyboardMarkup()
        join_button = InlineKeyboardButton("Приєднатися до гри", callback_data='join_game',
                                           url="https://t.me/newspygame_bot?start=join_game")
        reply_markup.add(join_button)

        message_builder = "<b>Проводиться набір у гру!</b>\n\nЗареєстровані гравці:\n"
        for user in users:
            message_builder += f"{user.first_name}\n"
        message_builder += f"Кількість гравців: {len(users)}"

        prev_msg = game1.get_messages()

        msg2 = bot.edit_message_text(
            message_builder,
            chat_id=prev_msg.chat.id,
            message_id=prev_msg.message_id,
            reply_markup=reply_markup,
            parse_mode="HTML")

        messages.append(msg2)
        game1.set_messages(msg2)

        times = time.time()

        game1.set_reg_list(times)

        _registrations.append(times)
        registration_time()

def registration_time():
    if game1.get_reg_list() and (time.time() - game1.get_reg_list()) >= 15:
        print("Час реєстрації минув. Починаємо гру!")
        game1.set_reg_status(False)
        prepearing()

def check_registration():
    while game1.get_reg_status():
        registration_time()
        time.sleep(1)

registration_thread = threading.Thread(target=check_registration)
registration_thread.start()

def prepearing():
    msg = game1.get_messages()
    if not game1.get_reg_status():
        bot.delete_message(msg.chat.id, msg.message_id)
        msg3 = bot.send_message(msg.chat.id, 'ГРА ПОЧАЛАСЬ!')

        global random_location
        random_location = random.choice(locations)

        # Надаємо ролі гравцям
        assign_roles(random_location)

        for player in players2:
            if player.role == 'Spy':
                bot.send_message(player.id,f"Ваша роль: Шпигун!")
            if player.role == 'NotSpy':
                bot.send_message(player.id,f"Ваша роль: Не шпигун.\nВаша локація: {random_location}!")

        start_game_timer()
        time.sleep(5)
        bot.delete_message(msg3.chat.id, msg3.message_id)


def assign_roles(random_location):
    user_ids = [user.id for user in users]

    spy_id = random.choice(user_ids)

    global spy_list
    spy_list.append(spy_id)

    # Присвоюємо ролі гравцям
    for user in users:
        if user.id == spy_id:
            players2.append(Player(user.id, user.username, user.first_name, 'Spy', random_location))

        else:
            players2.append(Player(user.id,user.username,user.first_name,'NotSpy',random_location))


@bot.message_handler()
def echo(message):
    print(
        f"{message.chat.type} | {message.chat.title} | {message.chat.id} | {message.from_user.first_name} | {message.text}")

    spy = None
    if spy_list:
        spy = spy_list[0]

    if message.from_user.id == spy:
        player_location = message.text
        correct_location = random_location

        if player_location == correct_location and player_location in locations:
            msg = bot.send_message(message.chat.id,f'Spy win! The spy was {message.from_user.first_name}' )
            clearing()
            time.sleep(10)
            bot.delete_message(message.chat.id, msg.message_id)

        if player_location != correct_location and player_location in locations:
            msg = bot.send_message(message.chat.id,f'Spy lost! The spy was {message.from_user.first_name}')
            clearing()
            time.sleep(10)
            bot.delete_message(message.chat.id, msg.message_id)

def start_game_timer():
    global game_timer
    game_timer = threading.Timer(20, end_game)
    game_timer.start()

def end_game():
    print("Час гри минув!")
    global game_ended
    game_ended = True
    bot.send_message(game1.get_messages().chat.id, "Час гри минув!")
    clearing()

bot.polling(none_stop=True)
