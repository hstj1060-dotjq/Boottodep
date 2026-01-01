from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8552719254:AAFRZ_B2sUP5foKQ71vzjevwOuHa5nqy2hs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📅 جدول المحاضرات", callback_data="schedule")],
        [InlineKeyboardButton("📚 الكتب", callback_data="books")],
        [InlineKeyboardButton("📝 التحاضير", callback_data="preparations")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "أهلاً بك 🌿\nاختر من القائمة 👇",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "schedule":
        await query.edit_message_text("📅 جدول المحاضرات سيضاف قريبًا")
    elif query.data == "books":
        await query.edit_message_text("📚 قسم الكتب")
    elif query.data == "preparations":
        await query.edit_message_text("📝 التحاضير")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()