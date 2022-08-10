import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend, Write the 'price' to find out the cost of the most popular "
                                          "crypto coins!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req_btc = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                req_eth = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response_btc = req_btc.json()
                response_eth = req_eth.json()
                sell_price_btc = response_btc["btc_usd"]["sell"]
                sell_price_eth = response_eth["eth_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price_btc}\nSell ETH price: {sell_price_eth} "
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Something was wrong"
                )
        else:
            bot.send_message(message.chat.id, "Check the command")
    bot.polling()


if __name__ == '__main__':
    #get_data()
    telegram_bot(token)
