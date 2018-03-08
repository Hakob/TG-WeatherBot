# Telegram Weather Bot
[Weather Bot](https://telegram.me/init_upbot) - The Weather In Your City

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installation

TG-Weather Bot requires [Python](https://www.python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ sudo apt install python3-pip
$ pip3 install virtualenv
$ cd ~ && git clone https://github.com/Hakob/TG-WeatherBot.git
$ cd TG-WeatherBot
$ virtualenv --python=python3 venv 
$ source bin/activate
(venv)$ pip3 install -r requirements.txt 
(venv)$ python3 main.py                   # Before this command, make sure that you provide 
                                          # weather_api_key and tg_token in main.py
```

## Deployment
For deployment this bot requires two token-variables, which we'll apply in the [_main.py_](main.py) file.
Add additional notes about how to bring these token respectively for:
*_weather_api_key_* and *_tg_token_* variables. (See 10, 11 lines in main.py)

  - [Telegram Bot Token Guide](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
  - [Open Weather API key Guide](https://openweathermap.org/appid)

## Built With

* [Requests](http://docs.python-requests.org/en/master/) - HTTP for Humans
* [OpenWeatherMap](https://openweathermap.org/api) - Open Weather Map API
* [TG Bots](https://core.telegram.org/bots/api) - Telegram Bot API

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

