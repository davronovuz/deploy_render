import asyncio
from datetime import datetime, timedelta
from aiogram import Router, types, F, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import ChatPermissions, BufferedInputFile

# 1. Router yaratamiz (Guruh bo'limi)
router = Router()

# 2. Faqat guruhlarda ishlashi uchun filtr qo'yamiz
router.message.filter(F.chat.type.in_({"group", "supergroup"}))

# --- 1. GURUH NOMINI O'ZGARTIRISH ---
@router.message(Command("setname"))
async def set_group_name(message: types.Message, command: CommandObject):
    if not command.args:
        return await message.answer("📝 Nom kiriting. Masalan: `/setname Yangi Guruh`")

    await message.chat.set_title(command.args)
    await message.answer("✅ Guruh nomi o'zgartirildi!")

# --- 2. GURUH TAVSIFINI O'ZGARTIRISH ---
@router.message(Command("setdesc"))
async def set_group_desc(message: types.Message, command: CommandObject):
    if not command.args:
        return await message.answer("📝 Tavsif kiriting. Masalan: `/setdesc Bu bizning guruh`")

    await message.chat.set_description(command.args)
    await message.answer("✅ Guruh tavsifi yangilandi!")

# --- 3. GURUH RASMINI O'ZGARTIRISH ---
@router.message(Command("setphoto"))
async def set_group_photo(message: types.Message, bot: Bot):
    # Rasmga reply qilinganini tekshiramiz
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.answer("🖼 Rasmga reply qilib /setphoto deb yozing!")

    # Rasmni yuklab olish jarayoni
    photo = message.reply_to_message.photo[-1]
    file = await bot.get_file(photo.file_id)
    content = await bot.download_file(file.file_path)

    # Rasmni guruhga o'rnatish
    photo_file = BufferedInputFile(content.read(), filename="group.jpg")
    await message.chat.set_photo(photo=photo_file)
    await message.answer("✅ Guruh rasmi yangilandi!")

# --- 4. FOYDALANUVCHINI BAN QILISH ---
@router.message(Command("ban"))
async def ban_user(message: types.Message):
    if not message.reply_to_message:
        return await message.answer("⚠️ Kimni haydaymiz? Xabariga reply qiling!")

    await message.chat.ban(user_id=message.reply_to_message.from_user.id)
    await message.answer(f"🚫 {message.reply_to_message.from_user.full_name} guruhdan chiqarib yuborildi!")

# --- 5. FOYDALANUVCHINI MUTE QILISH ---
@router.message(Command("mute"))
async def mute_user(message: types.Message, command: CommandObject):
    if not message.reply_to_message:
        return await message.answer("⚠️ Kimni mute qilamiz? Xabariga reply qiling!")

    # Vaqtni olish (agar yozilmagan bo'lsa 5 daqiqa)
    vagt = 5
    if command.args and command.args.isdigit():
        vagt = int(command.args)

    tugash_vaqti = datetime.now() + timedelta(minutes=vagt)

    # Huquqlarni cheklash
    await message.chat.restrict(
        user_id=message.reply_to_message.from_user.id,
        permissions=ChatPermissions(can_send_messages=False),
        until_date=tugash_vaqti
    )
    await message.answer(f"🔇 Foydalanuvchi {vagt} daqiqaga yozishdan to'sildi.")

# --- 6. XABARNI O'CHIRISH ---
@router.message(Command("del"))
async def delete_message(message: types.Message):
    if message.reply_to_message:
        await message.reply_to_message.delete() # Tanlangan xabarni o'chirish
        await message.delete() # /del komandasini o'chirish

# --- 7. YANGI A'ZOLARNI QUTLASH ---
@router.message(F.new_chat_members)
async def welcome(message: types.Message):
    for user in message.new_chat_members:
        await message.answer(f"Xush kelibsiz, {user.full_name}! 👋")