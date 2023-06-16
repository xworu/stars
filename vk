from social_spam import Vkontakte
import schedule
import time
import os

user_token = os.getenv("VK_TOKEN")
# a personal token of your account with access to messages, friends and access at any time.

vk = Vkontakte()
vk.connect_user(token=user_token)
# The token can be obtained from the link: https://vkhost.github.io/


def everyday_horoscope():
    name = vk.get_name_by_id(434344214)['first_name']
    vk.send_message(434344214, message=f'Hi, {name}! Horoscope advises you...', image='./image.png')
    print("Message was sent successfully.")


schedule.every().day.at("07:00").do(everyday_horoscope)

while True:
    schedule.run_pending()
    time.sleep(1)
