from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("", "Пообщаться с техподдержкой"),
        types.BotCommand("help", "Помощь"),
    ])