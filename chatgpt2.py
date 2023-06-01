import os
import telegram
import telebot
import openai
from dotenv import load_dotenv

load_dotenv()

# Set up Telegram bot and OpenAI API credentials
telegram_token = os.getenv('5992173735:AAEGdQ-N6bKGDU2HcusWZitnyvx1ZOneGhM')
openai_api_key = os.getenv('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')
bot = telebot.TeleBot("5992173735:AAEGdQ-N6bKGDU2HcusWZitnyvx1ZOneGhM")​
openai.api_key = openai_api_key

# Define the function that generates response using GPT-3.5
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

# Define the function that handles incoming messages
def message_handler(update, context):
    chat_id = update.message.chat_id
    user_message = update.message.text
    
    # Call GPT-3.5 with user input as prompt
    gpt_response = generate_response(user_message)
    
    # Send response back to user
    bot.send_message(chat_id=chat_id, text=gpt_response)

# Set up the message handler and start the bot
bot_dispatcher = telegram.ext.Dispatcher(bot, None, workers=0)
bot_dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))
bot_updater = telegram.ext.Updater(bot=bot, use_context=True, dispatcher=bot_dispatcher)
bot_updater.start_polling()
