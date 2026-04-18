from aiogram import Router, html
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    InlineQueryResultCachedVideo,
    InlineQueryResultVideo
)
import uuid

# Router yaratamiz
inline_router = Router()


@inline_router.inline_query()
async def main_inline_handler(query: InlineQuery):
    # Foydalanuvchi kiritgan matnni tozalaymiz
    user_query = query.query.lower().strip()
    results = []

    # 1. RASM YUBORISH (Agar 'rasm' deb yozsa)
    if user_query == "rasm":
        results.append(
            InlineQueryResultPhoto(
                id=str(uuid.uuid4()),  # Takrorlanmas ID yaratish
                photo_url="https://picsum.photos/800/600",
                thumbnail_url="https://picsum.photos/200/200",
                title="Premium Tasodifiy Rasm",
                description="Chatga yuborish uchun ustiga bosing",
                caption=f"🖼 {html.bold('Tasodifiy sifatli rasm')}\n\nUshbu rasm inline rejimda yuborildi.",
                parse_mode="HTML"
            )
        )

    # 2. VIDEO YUBORISH (file_id orqali - eng tez usul)
    elif user_query == "video":
        # Diqqat: Bu yerga o'zingizning botingizdagi haqiqiy file_id ni qo'ying
        VIDEO_FILE_ID = "BAACAgIAAxkBAAI..."

        results.append(
            InlineQueryResultCachedVideo(
                id=str(uuid.uuid4()),
                video_file_id=VIDEO_FILE_ID,
                title="Siz kutgan video darslik",
                description="Telegram serveridan tezkor yuklanadi",
                caption="🎥 {html.italic('Darslik videosi')}\n\nMuvaffaqiyatli yuborildi!",
                parse_mode="HTML"
            )
        )

    # 3. MATNNI TESKARI QILISH (Agar matn 'rasm' yoki 'video' bo'lmasa va bo'sh bo'lmasa)
    elif user_query:
        reversed_text = user_query[::-1]
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Matnni teskari qilish",
                description=f"Natija: {reversed_text}",
                input_message_content=InputTextMessageContent(
                    message_text=f"🔄 {html.code(user_query)} so'zining teskarisi: {html.bold(reversed_text)}",
                    parse_mode="HTML"
                )
            )
        )

    # 4. YORDAM MENYUSI (Agar qidiruv bo'sh bo'lsa)
    else:
        results.append(
            InlineQueryResultArticle(
                id="help_info",
                title="Inline Botdan foydalanish",
                description="'rasm', 'video' deb yozing yoki shunchaki matn kiriting",
                input_message_content=InputTextMessageContent(
                    message_text=f"🤖 {html.bold('Inline Bot Yordamchisi')}\n\n"
                                 f"Quyidagi buyruqlarni yozib ko'ring:\n"
                                 f"1. {html.code('rasm')} - Tasodifiy rasm olish\n"
                                 f"2. {html.code('video')} - Video yuborish\n"
                                 f"3. {html.code('matn')} - Matnni teskari qilish",
                    parse_mode="HTML"
                )
            )
        )

    # Natijalarni yuborish
    # cache_time=1 - natijalar tez yangilanishi uchun
    # is_personal=True - har bir foydalanuvchi o'ziga xos natija olishi uchun
    await query.answer(results=results, cache_time=1, is_personal=True)




    from aiogram.types import InlineQuery, InlineQueryResultPhoto, InlineQueryResultGif, InlineQueryResultArticle, InputTextMessageContent
import uuid

@inline_router.inline_query()
async def multi_result_handler(query: InlineQuery):
    user_query = query.query.lower().strip()
    results = []

    if user_query == "shou":
        # 1-rasm
        results.append(
            InlineQueryResultPhoto(
                id=str(uuid.uuid4()),
                photo_url="https://picsum.photos/id/10/800/600",
                thumbnail_url="https://picsum.photos/id/10/200/200",
                title="Tabiat manzarasi",
                caption="Bu birinchi rasm"
            )
        )
        
        # 2-rasm
        results.append(
            InlineQueryResultPhoto(
                id=str(uuid.uuid4()),
                photo_url="https://picsum.photos/id/20/800/600",
                thumbnail_url="https://picsum.photos/id/20/200/200",
                title="Boshqa manzara",
                caption="Bu ikkinchi rasm"
            )
        )

        # GIF yuborish
        results.append(
            InlineQueryResultGif(
                id=str(uuid.uuid4()),
                gif_url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZueXF4Znd4Znd4Znd4Znd4/3o7TKsQ8g48S95vK0M/giphy.gif",
                thumbnail_url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZueXF4Znd4Znd4Znd4Znd4/3o7TKsQ8g48S95vK0M/giphy.gif",
                title="Quvnoq GIF",
                caption="Inline rejimda yuborilgan GIF!"
            )
        )

    await query.answer(results=results, cache_time=1)