from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# توضع هنا توكن البوت
TOKEN = "8552719254:AAFRZ_B2sUP5foKQ71vzjevw OuHa5nqy2hs"

# دالة /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("ملخصات", callback_data='summary')],
        [InlineKeyboardButton("كتب", callback_data='books')],
        [InlineKeyboardButton("ملازم", callback_data='notebooks')],
        [InlineKeyboardButton("الجدول", callback_data='schedule')],
        [InlineKeyboardButton("ملفات مهمة", callback_data='important_files')],
        [InlineKeyboardButton("مواقع مفيدة", callback_data='useful_sites')],
        [InlineKeyboardButton("تطبيقات مفيدة", callback_data='useful_apps')],
        [InlineKeyboardButton("حول البوت", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("مرحبًا بك في بوت طلبة المرحلة الأولى! اختر أحد الخيارات:", reply_markup=reply_markup)

# التعامل مع أزرار القائمة
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == "summary":
        query.edit_message_text(text="📄 هذه صفحة الملخصات. يمكنك رفع أو تحميل الملخصات هنا.")
    elif query.data == "books":
        query.edit_message_text(text="📚 هذه صفحة الكتب المتاحة للمرحلة الأولى.")
    elif query.data == "notebooks":
        query.edit_message_text(text="📝 هذه صفحة الملازم.")
    elif query.data == "schedule":
        query.edit_message_text(text="📅 هذا هو الجدول الدراسي للمرحلة الأولى.")
    elif query.data == "important_files":
        query.edit_message_text(text="📁 الملفات المهمة الخاصة بالمرحلة الأولى.")
    elif query.data == "useful_sites":
        query.edit_message_text(text="🌐 هذه مواقع مفيدة للطلاب.")
    elif query.data == "useful_apps":
        query.edit_message_text(text="📱 هذه تطبيقات مفيدة للطلاب.")
    elif query.data == "about":
        query.edit_message_text(text="🤖 حول البوت: هذا البوت مخصص لمساعدة طلاب المرحلة الأولى.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    
    print("البوت شغال...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
