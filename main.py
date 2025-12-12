
# Катаула Владислав ІПЗ 2.01

import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_marked_section, as_list, Bold, Italic
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties


from kbds import (
    main_keyboard,
    builder_menu,
    phone_location_kbd,
    delete_keyboard,
)
from kbds import (
    main_keyboard,
    builder_menu,
    phone_location_kbd,
    delete_keyboard,
)


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


dp = Dispatcher(bot=bot)



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "<b>Вітаю!</b> \n<i>Оберіть пункт меню.</i>",
        reply_markup=main_keyboard,
    )


@dp.message(F.text.lower() == "про мене")
async def about(message: types.Message):
    items = ["Історія створення", "Донати на їжу"]
    menu = await builder_menu(items)

    await message.answer(
        "<u>Розділ «Про мене»</u>",
        reply_markup=menu.as_markup(resize_keyboard=True),
    )


@dp.message(F.text.lower() == "донати на їжу")
async def payment(message: types.Message):
    await message.answer(
        "<b>Оплата</b> можлива карткою або криптовалютою.",
        reply_markup=main_keyboard,
    )


@dp.message(F.text.lower() == "відправити дані")
async def send_data(message: types.Message):
    await message.answer(
        "<i>Оберіть, що надіслати:</i>",
        reply_markup=phone_location_kbd.as_markup(resize_keyboard=True),
    )


@dp.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(
        f"<b>Телефон отримано:</b> {message.contact.phone_number}"
    )


@dp.message(F.location)
async def get_location(message: types.Message):
    await message.answer(
        f"<b>Локація отримана:</b>\n"
        f"{message.location.latitude}, {message.location.longitude}"
    )


@dp.message(F.text.lower() == "вийти")
async def remove_keyboard(message: types.Message):
    await message.answer(
        "<s>Клавіатуру прибрано.</s>",
        reply_markup=delete_keyboard,
    )



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())