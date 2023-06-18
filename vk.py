from generation_for_sending import zodiac_signs
from social_spam import Vkontakte
import schedule
from datetime import date
import time
import os
import psycopg2

conn = psycopg2.connect(database="stars",
                        user="postgres",
                        password=" ",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

user_token = os.getenv("VK_TOKEN")
# a personal token of your account with access to messages, friends and access at any time.

vk = Vkontakte()
vk.connect_user(token=user_token)
# The token can be obtained from the link: https://vkhost.github.io/


def everyday_horoscope(records):
    id = records[0][6]
    sign = records[0][5]
    current_date = date.today()
    name = vk.get_name_by_id(id)['first_name']
    horoscope = zodiac_signs[sign]
    vk.send_message(id, message=f'Доброго утра, {name}! {current_date.day}.{current_date.month}.{current_date.year} {horoscope}', image='./image.png')
    print("Message was sent successfully.")


def vk_sending():
    cursor.execute("SELECT * FROM user_info WHERE vk_id is not null")
    records = list(cursor.fetchall())
    for i in records:
        everyday_horoscope(records)


schedule.every().day.at("07:00").do(vk_sending)

while True:
    schedule.run_pending()
    time.sleep(1)
