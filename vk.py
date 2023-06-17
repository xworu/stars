from main import generate_horoscope
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
    current_date = date.today()
    name = vk.get_name_by_id(id)['first_name']
    horoscope = generate_horoscope()
    vk.send_message(id, message=f'Доброго утра, {name}! {current_date} {horoscope}', image='./image.png')
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

