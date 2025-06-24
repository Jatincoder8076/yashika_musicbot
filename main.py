
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from admin import gban, gunban, gbroadcast
from keep_alive import keep_alive
import random

TOKEN = os.environ.get("TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))

STICKERS = [
    "CAACAgUAAxkBAAEDjYZlksr5cCatIDsl8grG7gbk5W6GRQACVwEAAkpw2VZmsSGO2vIm3CAE",
    "CAACAgUAAxkBAAEDjYdlksr6JPn43mBDgoFRTG7Tru0uSgACWAEAAkpw2VZkhR0cfZK0gyAE"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = f"╭───────────────────▣\n"                    f"│❍ ʜᴇʏ {user_name} •\n"                    f"│❍ ɪ ᴀᴍ ˹𝙔ᴀꜱʜɪᴋᴀ ✘ 𝙈ᴜꜱɪᴄ˼ ♪ •\n"                    f"├───────────────────▣\n"                    f"│❍ ʙᴇsᴛ ǫᴜɪʟɪᴛʏ ғᴇᴀᴛᴜʀᴇs •\n"                    f"│   sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ \n"                    f"╰───────────────────▣"
    keyboard = [[
        InlineKeyboardButton("OWNER", url="https://t.me/myself_jatin"),
        InlineKeyboardButton("ABOUT", callback_data='about')
    ],[
        InlineKeyboardButton("SUPPORT", url="https://t.me/+Gi_cJroWWzxkZDJl")
    ]]
    await update.message.reply_photo(
        photo="https://telegra.ph/file/4fda420d4df4b2dd68e94.jpg",
        caption=welcome_text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def ajar_hear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker = random.choice(STICKERS)
    await update.message.reply_sticker(sticker)

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎧 Searching your song...")
    sticker = random.choice(STICKERS)
    await update.message.reply_sticker(sticker)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 Welcome {member.mention_html()} to *Yashika Zone*! 💖",
            parse_mode="HTML"
        )

if __name__ == "__main__":
    keep_alive()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play_command))
    app.add_handler(CommandHandler("gban", gban))
    app.add_handler(CommandHandler("gunban", gunban))
    app.add_handler(CommandHandler("gbroadcast", gbroadcast))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'^(ajar|hear)$'), ajar_hear))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.run_polling()
