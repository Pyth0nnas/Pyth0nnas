
#!/usr/bin/env python3
"""
Telegram bot for finding the spirit animal and zodiac sign.
"""

import logging
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    ContextTypes
)

from config import BOT_TOKEN
from zodiac_data import get_chinese_zodiac, get_western_zodiac, get_fun_fact

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# dialog condition
BIRTHDATE = 0

# reply keyboard
reply_keyboard = [['/start', '/help'], ['/cancel']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"🌟 Hello, {user_name}!\n\n"
        "Send me your birth date in this format - **00.00.0000**\n"
        "Example: `15.03.1995`",
        parse_mode='Markdown',
        reply_markup=markup
    )
    return BIRTHDATE

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 **Instructions:**\n\n"
        "1. /start - To start\n"
        "2. Enter birth date \n"
        "3. Discover your spirit animal and your zodiac sign!\n\n"
        "/cancel - To cancel",
        parse_mode='Markdown'
    )

async def handle_birthdate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    try:
        day, month, year = map(int, text.split('.'))
        datetime(year, month, day)  # validation
        
        chinese = get_chinese_zodiac(year)
        western = get_western_zodiac(month, day)
        
        response = (
            f"📅 **Date:** {day:02d}.{month:02d}.{year}\n\n"
            f"🐉 **Chinese:** {chinese}\n"
            f"✨ **Western:** {western}\n\n"
            f"🌟 {get_fun_fact(chinese, western)}"
        )
        
        await update.message.reply_text(response, parse_mode='Markdown')
        
    except ValueError:
        await update.message.reply_text(
            "❌ Incorrect input! Valid input format - 00.00.0000\n"
            "example: `15.03.1995`",
            parse_mode='Markdown'
        )
    
    return BIRTHDATE

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('👋 Goodbye!', reply_markup=markup)
    return ConversationHandler.END

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤔 Unknown command. Use /start or /help")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            BIRTHDATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_birthdate)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("🤖 Bot is active! press Ctrl+C to stop it")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

