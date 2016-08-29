from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from quotes import jojoquotes
import random
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('settings.ini')

token = parser.get('main','token')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

print(
    '******Bot started******',
    '\nToken: {}'.format(token),
    )


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def say(bot, update):
    bot.sendMessage(update.message.chat_id, text=random.choice(jojoquotes))


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=random.choice(jojoquotes))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("help", help))
    dp.addHandler(CommandHandler("say", say))

    # on noncommand i.e message - echo the message on Telegram
    dp.addHandler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()