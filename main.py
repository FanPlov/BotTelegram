import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Получаем токен из настроек Railway (Environment Variables)
TOKEN = os.getenv("BOT_TOKEN")
# Ссылка на твой сайт (замени на свою реальную ссылку)
WEB_APP_URL = "https://subtle-malabi-1fcd38.netlify.app/" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Создаем кнопку для открытия Mini App
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🍕 Pizza Academy", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в <b>Pizza Academy</b>.\n"
        "Нажми на кнопку ниже, чтобы выбрать время для урока 👇",
        reply_markup=markup,
        parse_mode="HTML"
    )

async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
