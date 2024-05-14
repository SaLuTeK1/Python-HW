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

random_location = ''
game_timer = None
spy_list = []
users = []
players2 = []

class User():
    def __init__(self,id,username,first_name):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.in_game = False

    def set_in_game(self,in_game):
        self.in_game = in_game

    def get_in_game(self):
        return self.in_game

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

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

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
    global players2,spy_list,random_location,users,players2,game1,game_timer
    players2 =[]
    game1 = Game(status=True,reg_status=True)
    spy_list = []
    users = []
    random_location = ''
    game_timer = None

@bot.message_handler(commands=['start'])
def connect_the_game(message):
    if message.chat.type == 'private':
        if 'join_game' in message.text.lower():
            if message.from_user.id not in [player.id for player in players2] and not [player.in_game for player in players2]:
                user_id = message.from_user.id
                username = message.from_user.username
                first_name = message.from_user.first_name

                users.append(User(user_id,username,first_name))

                join_game()

                bot.send_message(message.chat.id, "Ти в ігрі, друже!", reply_to_message_id=message.message_id)

            elif [player.in_game for player in players2]:
                bot.send_message(message.chat.id, "Ти вже в ігрі!", reply_to_message_id=message.message_id)

        else:
            bot.send_message(message.chat.id, f'Вітаю, {message.from_user.first_name}!')

@bot.message_handler(commands=['locations'])
def locations_list(message):

    bot.send_message(message.chat.id, '\n'.join(locations))

@bot.message_handler(commands=['game'])
def start_the_game(message):
    bot.delete_message(message.chat.id, message.message_id)

    reply_markup = InlineKeyboardMarkup()

    join_button = InlineKeyboardButton("Приєднатися до гри", callback_data='join_game',
                                       url="https://t.me/newspygame_bot?start=join_game")
    reply_markup.add(join_button)

    msg1 = bot.send_message(
        message.chat.id,
        "Привіт! Я бот для гри Шпигун. Щоб приєднатися до гри, натисни кнопку нижче.",
        reply_markup=reply_markup
    )

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

        game1.set_messages(msg2)

        times = time.time()

        game1.set_reg_list(times)

        registration_thread = threading.Thread(target=check_registration)
        registration_thread.start()

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
                player.set_in_game(True)
            if player.role == 'NotSpy':
                bot.send_message(player.id,f"Ваша роль: Не шпигун.\nВаша локація: {random_location}!")
                player.set_in_game(True)

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
        global starter

        if player_location == correct_location and player_location in locations:
            msg = bot.send_message(message.chat.id,f'Spy win! The spy was {message.from_user.first_name}' )
            game1.set_status(False)
            start_game_timer()
            time.sleep(10)
            bot.delete_message(message.chat.id, msg.message_id)

        if player_location != correct_location and player_location in locations:
            msg = bot.send_message(message.chat.id,f'Spy lost! The spy was {message.from_user.first_name}')
            game1.set_status(False)
            start_game_timer()
            time.sleep(10)
            bot.delete_message(message.chat.id, msg.message_id)

def start_game_timer():
    status = game1.get_status()
    global game_timer

    if status == True:
        game_timer = threading.Timer(40, end_game)
        game_timer.start()

    elif status == False:
        if game_timer is not None:
            game_timer.cancel()
            clearing()

def end_game():
    print(game1.get_status())
    if game1.get_status():
        print("Час гри минув!")
        bot.send_message(game1.get_messages().chat.id, "Час гри минув!")
        clearing()

bot.polling(none_stop=True)
