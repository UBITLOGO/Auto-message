import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

AGENCY = "Crypto Listing Hub"
ADMIN = os.getenv("ADMIN_USERNAME", "youradmin")
GROUP = os.getenv("TELEGRAM_GROUP", "")

WELCOME = f"""🚀 Welcome to {AGENCY}!

We help crypto projects with:
• ✅ Tier-1 & Tier-2 Exchange Listings
• ✅ CoinMarketCap & CoinGecko Listings
• ✅ Marketing & Trending Campaigns
• ✅ MM Bots & Liquidity
• ✅ Automation Bots & DB Outreach

👤 Contact: @{ADMIN}
{'📣 Group: ' + GROUP if GROUP else ''}
Type 'services' anytime to see full services.
"""

SERVICES = f"""📋 Services – {AGENCY}
• Exchange Listings: Tier-1 & Tier-2
• CMC/CG Listings & Data setup
• Marketing, KOLs, AMAs, Trending
• MM Bots, Liquidity & Growth
👤 Admin: @{ADMIN}
"""

def cmd_start(update, context):
    update.message.reply_text(WELCOME)

def on_text(update, context):
    txt = (update.message.text or "").lower()
    if "services" in txt:
        update.message.reply_text(SERVICES)
    else:
        update.message.reply_text(WELCOME)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise SystemExit("BOT_TOKEN missing")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", cmd_start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, on_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
