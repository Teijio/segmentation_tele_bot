import os
from typing import Final

import telebot
from telebot import types
from dotenv import load_dotenv

from start import get_names, delete_bg

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_USERNAME: Final = "@photo_lolo_bot"

bot = telebot.TeleBot(TOKEN)

image_path = "./images/image.jpg"
seg_image = "./images/seg_image.png"

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {message.from_user.first_name}, скиньте мне любую фотографию",
    )


@bot.message_handler(content_types=["text"])
def ans(message):
    bot.send_message(message.chat.id, "Я принимаю только фото.")


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file_info = bot.get_file(file_id)
    downloaded_photo = bot.download_file(file_info.file_path)
    image_path = "./images/image.jpg"  # Путь для сохранения фото
    with open(image_path, "wb") as new_file:
        new_file.write(downloaded_photo)
    names = get_names(image_path)
    markup = types.InlineKeyboardMarkup()
    if names:
        for name, prob, name_id in names:
            button = types.InlineKeyboardButton(f"{name} id {prob}", callback_data=str(name_id))
            markup.add(button)
        with open("./segment/predict/image.jpg", "rb") as photo_file:
            bot.send_photo(
                message.chat.id, photo_file, caption="Можно вырезать:", reply_markup=markup
            )
    else:
        button = types.InlineKeyboardButton(
            "Удали меня", callback_data="delete"
        )
        markup.add(button)
        bot.reply_to(message, "ничего не найдено:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.message:
        if call.data == "delete":
            bot.delete_message(
                call.message.chat.id, call.message.message_id - 1
            )
            bot.delete_message(call.message.chat.id, call.message.message_id)
        else:
            name_id = int(call.data)
            delete_bg(image_path, name_id)
            with open(seg_image, "rb") as photo_file:
                bot.send_photo(
                    call.message.chat.id, photo_file, caption="как-то так"
                )


bot.polling(none_stop=True)
