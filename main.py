#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
from time import sleep

from BotHandler import BotHandler
from WeatherHandler import WeatherHandler

weather_api_key = 'd9925fdb475f8195a8e7ad7fff0a766b'
tg_token = '509190040:AAGuckU0iDAnq-l6lXpdDfRy1kcqjxBeyfA'

weather_handler = WeatherHandler(api_key=weather_api_key)
greet_bot = BotHandler(token=tg_token)
now = datetime.datetime.now()
hour = now.hour


def main():
    last_update = greet_bot.get_updates()['result'][-1]
    last_id = last_update['update_id']
    last_chat_id = last_update['message']['chat']['id']
    last_chat_name = last_update['message']['chat']['first_name']
    if 6 <= hour < 12:
        greet_bot.send_message(last_chat_id, 'Good Morning {}'.format(last_chat_name))

    elif 12 <= hour < 17:
        greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))

    elif 17 <= hour < 23:
        greet_bot.send_message(last_chat_id, 'Good Evening {}'.format(last_chat_name))

    else:
        greet_bot.send_message(last_chat_id, 'Good Night {}'.format(last_chat_name))

    while True:
        last = greet_bot.get_updates(offset=-1)
        last = last['result'][-1]
        last_update_id = last['update_id']

        if last_update_id == last_id:
            sleep(3)
            continue
        else:
            last_id = last_update_id
            last_chat_text = last['message']

        if 'text' in last_chat_text.keys():
            last_text = last_chat_text['text'].lower()

            if last_text == '/start':
                greet_bot.get_location(last_chat_id)
                sleep(3)
                continue

            elif last_text == 'cancel':
                greet_bot.send_message(last_chat_id, "*Canceled.*\nSend me name of your city")
                sleep(5)
                continue

            else:
                res = weather_handler.by_city(city_name=last_text)
                if res['cod'] == '404':
                    res = res['message']
                    greet_bot.send_message(last_chat_id, "*" + res.capitalize() + "*\nPlease try again...")
                    sleep(5)
                    continue
                res_weather = res['weather'][-1]
                res_main = res['main']
                formatted_caption = '*City: {0}*\n\n*{1}*\n_{2}_\n*Temperature:* {3}_°C_\n'\
                                    '*Pressure:* {4}_hPa_\n*Clouds:* {5}_%_\n*Humidity:* {6}_%_\n*Wind Speed:* {7}_m/s_'\
                    .format(res['name'], res_weather['main'], res_weather['description'], res_main['temp'],
                            res_main['pressure'], res['clouds']['all'], res_main['humidity'], res['wind']['speed'])

                greet_bot.render_info(last_chat_id, res_weather['icon'], formatted_caption)

        if 'location' in last_chat_text.keys():
            location = last_chat_text['location']
            res = weather_handler.by_location(location)
            res_weather = res['weather'][-1]
            res_main = res['main']
            formatted_caption = '*City: {0}*\n\n*{1}*\n_{2}_\n*Temperature:* {3}_°C_\n' \
                                '*Pressure:* {4}_hPa_\n*Clouds: {5}_%_*\n*Humidity:* {6}_%_\n*Wind Speed:* {7}_m/s_' \
                .format(res['name'], res_weather['main'], res_weather['description'], res_main['temp'],
                        res_main['pressure'], res['clouds']['all'], res_main['humidity'], res['wind']['speed'])
            greet_bot.render_info(last_chat_id, res_weather['icon'], formatted_caption)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
