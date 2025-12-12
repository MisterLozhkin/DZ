
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder



main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Про мене")],
        [KeyboardButton(text="Відправити дані"), KeyboardButton(text="Вийти")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Оберіть дію",
)



async def builder_menu(items):
    kbd = ReplyKeyboardBuilder()
    for i in items:
        kbd.add(KeyboardButton(text=i))
    return kbd.adjust(2)



phone_location_kbd = ReplyKeyboardBuilder()
phone_location_kbd.add(
    KeyboardButton(text="Надіслати номер телефону", request_contact=True),
    KeyboardButton(text="Надіслати локацію", request_location=True),
)
phone_location_kbd.adjust(2)



delete_keyboard = ReplyKeyboardRemove()
