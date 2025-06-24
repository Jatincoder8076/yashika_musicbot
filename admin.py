
from telegram import Update
from telegram.ext import ContextTypes

banned_users = set()

async def gban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != int(context.bot_data.get("OWNER_ID", 0)):
        return
    if context.args:
        user_id = int(context.args[0])
        banned_users.add(user_id)
        await update.message.reply_text(f"✅ User {user_id} has been globally banned.")
    else:
        await update.message.reply_text("⚠️ Provide a user ID to gban.")

async def gunban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != int(context.bot_data.get("OWNER_ID", 0)):
        return
    if context.args:
        user_id = int(context.args[0])
        banned_users.discard(user_id)
        await update.message.reply_text(f"✅ User {user_id} has been globally unbanned.")
    else:
        await update.message.reply_text("⚠️ Provide a user ID to gunban.")

async def gbroadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != int(context.bot_data.get("OWNER_ID", 0)):
        return
    msg = " ".join(context.args)
    if msg:
        await update.message.reply_text(f"📣 Broadcasting to all groups: {msg}")
    else:
        await update.message.reply_text("⚠️ Please provide a message to broadcast.")
