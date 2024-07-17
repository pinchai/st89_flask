import requests


def sendNotify(msg):
    bot_token = "6986363245:AAEKpwak_fBiBX9Pmy08IyxjuH1-_zf0Dqo"
    chat_id = "@st89_channel"

    html = msg

    html = requests.utils.quote(html)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
    res = requests.get(url)
    return res
