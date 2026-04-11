from aiogram.filters import Command,CommandObject
from aiogram.types import Message
import asyncio
from aiogram import types
from aiogram import F,Router,Bot


group_router=Router()

group_router.message.filter(F.chat.type.in_({"group","supergroup"}))

# Guruh title ni o'zgartiruvchi handler
@group_router.message(Command("settitle"))
async def set_title_group(message:types.Message,command:CommandObject):
    if not command.args:
        return await("Guruh nomini o'zgartirish uchun /settitle guruh nomi  yuboring")

    await message.chat.set_title(command.args)
    await message.answer("Guruh nomi muvaffaqiyatli o'zgartirildi .")


