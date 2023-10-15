from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot:Bot):
    commands = [
        BotCommand(
            command='/unic',
            description='все что связано с универом'
        ),
        BotCommand(
            command='/all',
            description='пингует всех'
        ),
        BotCommand(
            command='/bomb',
            description='мини игра где надо угадать один из проводков'
        ),
        BotCommand(
            command='/admin',
            description='Админ панель для добавления/редактирования/удаления чего либо'
        )
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault()) #юзать именно этот метод, для отображения для всех пользвателей