from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def _time(update, context):
    update.message.reply_text(str('Текущее время: ' + time.asctime().split()[3]))


def date(update, context):
    temp = time.asctime().split()
    update.message.reply_text(str(' '.join(["Текущая дата:",
                                           temp[1],
                                           temp[2],
                                           temp[4]])))


def echo(update, context):
    update.message.reply_text('Я получил сообщение ' + update.message.text)


def main():
    updater = Updater(token='1127285805:AAFl6hDKDOP68QW8B-uopFclFuuwpfJbQLw', use_context=True)  # нужен токен бота
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('time', _time))
    dp.add_handler(CommandHandler('date', date))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
