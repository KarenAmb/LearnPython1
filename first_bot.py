from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater('494529715:AAHrWdOiV6h035rOzJ6e3iI9nOdMkWkqGYk')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', user_welcomming))
    dp.add_handler(MessageHandler(Filters.text, talking_with_user))
    updater.start_polling()
    updater.idle()


def user_welcomming(bot, update):
    my_text = """Здарова {}!
Я только начал жить, не суди строго =)""".format(update.message.chat.first_name)
    print(my_text)
    update.message.reply_text(my_text)

def talking_with_user(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text+'. Окей, и что?')

if __name__ == "__main__":
    main()
