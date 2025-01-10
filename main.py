import asyncio


from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# INIT
bot = Bot(
    token="7651589086:AAE9qK4e2hli4U3b8CBIBTPkxW8FGko8TCw",
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
dp = Dispatcher()
engine = create_engine('mysql+pymysql://FrostByte:3PerXyks@0.0.0.0/database')
Base = declarative_base()
Session = sessionmaker(bind=engine)


@dp.message(Command('start'))
async def start_help_command(message: types.Message):
    await message.reply('\n\n<b>Приветствуем вас!</b>\n\nЯ — ваш помощник в управлении чатом. Моя основная цель — поддерживать порядок и комфортную атмосферу общения.\n\n<b>Что я умею делать:</b>\n\n Удалять нежелательные сообщения.\n Блокировать участников за нарушение правил.\n Предупреждать пользователей о недопустимом поведении.\n Предоставлять статистику активности чата.\n Помогать с настройками чата и управлением участниками.\n\nКак меня использовать:\n\n Просто напишите мне команду, и я сразу приступлю к выполнению задачи. Список доступных команд вы найдете, используя команду /help.\n\n<b>Важно:</b>\n\nЯ работаю исключительно по указаниям администраторов и модераторов чата. Если у вас возникнут вопросы или предложения, обращайтесь к ним напрямую.')


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply('Пока-что в разработке')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())