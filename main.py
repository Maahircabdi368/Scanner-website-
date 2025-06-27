from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import TelegramError

# Casharro muhiim ah (text + image)
lessons = {
    "Introduction": {
        "text": "🔐 *Introduction to Cyber Security*\n\nCybersecurity waa ilaalinta nidaamyada, shabakadaha iyo xogta weerarada dijitaalka ah. Waa difaac joogto ah oo lagula dagaalamo hanjabaadaha dijitaalka.\n\n👇 Si aad u sii wadato, dooro mowduuc hoosaad:",
        "photo": "https://i.imgur.com/hvjKxZY.png"
    },
    "Importance": {
        "text": "✅ *Importance of Cyber Security:*\n- Ilaalinta xogta gaarka ah\n- Ka hortag weerarada internetka\n- Kalsoonida nidaamka IT",
        "photo": "https://i.imgur.com/DG7A0Wp.jpg"
    },
    "Types": {
        "text": "🔍 *Noocyada Cybersecurity:*\n- Network Security\n- Application Security\n- Cloud Security\n- IoT Security",
        "photo": "https://i.imgur.com/NKRAOCj.jpg"
    },
    "Goals": {
        "text": "🎯 *Ujeedooyinka Cybersecurity:*\n- Confidentiality\n- Integrity\n- Availability\n\nWaxaa loo yaqaanaa CIA Triad.",
        "photo": "https://i.imgur.com/nDFbI2Y.jpg"
    },
    "Footprinting": {
        "text": "📘 *Footprinting* waa xog uruurin:\n- WHOIS\n- DNS Records\n- IP tools\n\n🛠 Tools: whois, nslookup, theHarvester.",
        "photo": "https://i.imgur.com/2XIM1Aw.png"
    },
    "Scanning": {
        "text": "📘 *Scanning* waa in la baaro IP/port:\n- Nmap\n- Netcat\n- TCP/UDP scan.",
        "photo": "https://i.imgur.com/wvhYO1D.png"
    },
}

contact_info = "\n\n❓ La xiriir Macallinka: @MaahirHacker"

# Bilaabista
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Introduction to Cyber Security", callback_data="Introduction")],
        [InlineKeyboardButton("Footprinting", callback_data="Footprinting")],
        [InlineKeyboardButton("Scanning", callback_data="Scanning")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="💻 Fadlan dooro casharka aad rabto inaad barato:", reply_markup=reply_markup)

# Marka cashar la doorto
async def lesson_chosen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except:
        pass  # Ignore timeout error on answering

    selected = query.data

    if selected == "start":
        await query.delete_message()
        await start(update, context)
        return

    if selected == "Introduction":
        lesson = lessons["Introduction"]
        buttons = [
            [InlineKeyboardButton("Importance", callback_data="Importance")],
            [InlineKeyboardButton("Types", callback_data="Types")],
            [InlineKeyboardButton("Goals", callback_data="Goals")],
            [InlineKeyboardButton("🔙 Dib u noqo", callback_data="start")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await context.bot.send_photo(
            chat_id=query.message.chat.id,
            photo=lesson["photo"],
            caption=lesson["text"],
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        await query.delete_message()
        return

    if selected in ["Importance", "Types", "Goals"]:
        lesson = lessons[selected]
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Dib u noqo", callback_data="Introduction")]
        ])
        await context.bot.send_photo(
            chat_id=query.message.chat.id,
            photo=lesson["photo"],
            caption=lesson["text"] + contact_info,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        await query.delete_message()
        return

    lesson = lessons.get(selected)
    if lesson:
        await context.bot.send_photo(
            chat_id=query.message.chat.id,
            photo=lesson["photo"],
            caption=lesson["text"] + contact_info,
            parse_mode='Markdown'
        )
        await query.delete_message()
    else:
        await query.edit_message_text("❌ Casharka lama helin.")

# Error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"🚨 ERROR: {context.error}")
    # Optional: update user
    if update and hasattr(update, "message"):
        try:
            await update.message.reply_text("❗ Khalad dhacay. Fadlan isku day mar kale.")
        except:
            pass

# Main
def main():
    TOKEN = "7996320421:AAEtL7AOgIEwpBCzMcoVhSLd25f3jMNlF1k"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(lesson_chosen))
    app.add_error_handler(error_handler)

    print("🤖 Bot-kuu wuu shaqaynayaa. Sug amarada...")
    app.run_polling()

if __name__ == "__main__":
    main()
