import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "9297828304:AAHeIVQTPDpELuGn7VkTUvIgWpcWNkOk4R4"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom! Signal botingiz muvaffaqiyatli ishga tushdi.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🚨 **TEST TRADING SIGNAL**\n\n"
        "📊 **Juftlik:** BTC/USDT\n"
        "📈 **Yo'nalish:** LONG\n"
        "🎯 **Kirish:** $90,500\n"
        "🛑 **Stop-Loss:** $89,000\n"
        "✅ **Take-Profit:** $93,000"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
