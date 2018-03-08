#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
from time import sleep

from BotHandler import BotHandler
from WeatherHandler import WeatherHandler

weather_api_key = '<open weather map api_key>'
tg_token = '<telegram bot token>'

weather_handler = WeatherHandler(api_key=weather_api_key)
greet_bot = BotHandler(token=tg_token)
now = datetime.datetime.now()
hour = now.hour


def main():
    last_update = greet_bot.get_updates(offset=-1)
    last_id = last_update['result'][-1]['update_id']

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

        last_chat_id = last['message']['chat']['id']
        last_keys = last_chat_text.keys()

        if 'text' in last_keys:
            last_text = last_chat_text['text'].lower()

            if last_text == '/start':
                greet_bot.get_location(last_chat_id)
                sleep(1)
                continue

            elif last_text == 'cancel':
                greet_bot.send_message(last_chat_id, "*Canceled.*\nSend me name of your city")
                sleep(1)
                continue

            else:
                res = weather_handler.by_city(city_name=last_text)
                if res['cod'] == '404':
                    res = res['message']
                    greet_bot.send_message(last_chat_id, "*" + res.capitalize() + "*\nPlease try again...")
                    sleep(1)
                    continue
                res_weather = res['weather'][-1]
                res_main = res['main']
                formatted_caption = '*City: {0}*\n\n*{1}*\n_{2}_\n*Temperature:* {3}_°C_\n' \
                                    '*Pressure:* {4}_hPa_\n*Clouds:* {5}_%_\n*Humidity:* {6}_%_\n*Wind Speed:* {7}_m/s_' \
                    .format(res['name'], res_weather['main'], res_weather['description'], res_main['temp'],
                            res_main['pressure'], res['clouds']['all'], res_main['humidity'], res['wind']['speed'])

                greet_bot.render_info(last_chat_id, res_weather['icon'], formatted_caption)

        if 'location' in last_keys:
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
