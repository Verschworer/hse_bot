import telebot
import pandas as pd
import config
from parser import write_df
from classifier import classified_write

bot = telebot.TeleBot(config.token)

write_df()
classified_write()
df = pd.read_csv(config.csv_classified)
df = df.head(10).filter(
    ['link',
     'classified',
     'probability',
     'title'],
    axis=1)

answer = '*И вот такие у нас новости*'
if not df.empty:
    for i in range(len(df)):
        answer = answer + '\n\n бот считает что с вероятностью ' \
                 + str((df['probability'].iloc[i]) * 100) + '%' \
                 + ' - ' + str((df['classified'].iloc[i])) \
                 + '\n\n' + str((df['link'].iloc[i]))


@bot.message_handler(commands=['start'])
def news_message(message):
    bot.send_message(message.chat.id, 'напишите /info для информации')

@bot.message_handler(commands=['info'])
def news_message(message):
    bot.send_message(message.chat.id, 'напишите боту /news и он попытается оценить '
                                      'достоверность десяти свежайших топиков с RSS Meduza.io.')


@bot.message_handler(content_types=['text'])
def news_messages(message):
    if message.text.lower() == '/news':
        bot.send_message(message.from_user.id, answer,
                         disable_web_page_preview=True)
    else:
        bot.send_message(message.from_user.id, 'напишите /news')


bot.polling(none_stop=True)
