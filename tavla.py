# tavla.py
from telegram import Update
from telegram.ext import CommandHandler

# Tavla oyunu komutları burada olacak

def tavla_game(update: Update, context) -> None:
    update.message.reply_text("Tavla oyununu başlatmak için /start yazın.")
