import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
TELEGRAM_GROUP = os.getenv("TELEGRAM_GROUP")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 Welcome to Crypto Listing Hub!\n\n"
        f"🌐 Group: {TELEGRAM_GROUP}\n"
        f"👤 Admin: @{ADMIN_USERNAME}\n\n"
        f"Type 'services' to see what we offer."
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Our Services:\n"
        "- ✅ Tier1 & Tier2 Exchange Listings\n"
        "- ✅ CoinMarketCap & CoinGecko Fast Listing\n"
        "- ✅ Marketing & Promotion Bots\n"
        "- ✅ Trending & Volume Boost\n\n"
        f"💬 Contact @{ADMIN_USERNAME} for details."
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "hi" in msg or "hello" in msg:
        await update.message.reply_text("👋 Hi! Welcome to Crypto Listing Hub. Type 'services' to see what we do.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    app.add_handler(MessageHandler(filters.Regex("services"), services))

    app.run_polling()

if __name__ == "__main__":
    main()
