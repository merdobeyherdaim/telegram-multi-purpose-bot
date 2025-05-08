from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import time
from config import API_KEY, OWNER, SERVER_OWNER

# Logging ayarları
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Başlangıç mesajı
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Merhaba! Benim adım Merdobey Bot. Yardım için /help yazabilirsiniz.")

# Yardım mesajı
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Bot komutları:\n/start - Başlat\n/help - Yardım")

# 12 saatte bir mesaj gönderme
def periodic_message(context: CallbackContext) -> None:
    context.bot.send_message(chat_id='@your_group', text=f"👑 Botun kurucusu: {OWNER}\n⚙️ Sunucu sahibi: {SERVER_OWNER}")

# Ana fonksiyon
def main() -> None:
    updater = Updater(API_KEY)

    # Dispatcher
    dp = updater.dispatcher

    # Komutlar
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # 12 saatte bir mesaj gönder
    job_queue = updater.job_queue
    job_queue.run_repeating(periodic_message, interval=43200, first=0)

    # Botu başlat
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
