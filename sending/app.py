from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="stars",
                        user="postgres",
                        password=" ",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/horoscope/', methods=['POST', 'GET'])
def subscription():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        date = request.form.get('date')
        bday = int(date[0:2])
        bmonth = int(date[3:5])

        if bday // 10 == 0:
            bday %= 10
        if bmonth // 10 == 0:
            bmonth %= 10

        if (bmonth == 1 and bday >= 20) or (bmonth == 2 and bday <= 18):
            zodiac_sign = "Водолей"
        elif (bmonth == 2 and bday >= 19) or (bmonth == 3 and bday <= 20):
            zodiac_sign = "Рыбы"
        elif (bmonth == 3 and bday >= 21) or (bmonth == 4 and bday <= 19):
            zodiac_sign = "Овен"
        elif (bmonth == 4 and bday >= 20) or (bmonth == 5 and bday <= 20):
            zodiac_sign = "Телец"
        elif (bmonth == 5 and bday >= 21) or (bmonth == 6 and bday <= 20):
            zodiac_sign = "Близнецы"
        elif (bmonth == 6 and bday >= 21) or (bmonth == 7 and bday <= 22):
            zodiac_sign = "Рак"
        elif (bmonth == 7 and bday >= 23) or (bmonth == 8 and bday <= 22):
            zodiac_sign = "Лев"
        elif (bmonth == 8 and bday >= 23) or (bmonth == 9 and bday <= 22):
            zodiac_sign = "Дева"
        elif (bmonth == 9 and bday >= 23) or (bmonth == 10 and bday <= 22):
            zodiac_sign = "Весы"
        elif (bmonth == 10 and bday >= 23) or (bmonth == 11 and bday <= 21):
            zodiac_sign = "Скорпион"
        elif (bmonth == 11 and bday >= 22) or (bmonth == 12 and bday <= 21):
            zodiac_sign = "Стрелец"
        else:
            zodiac_sign = "Козерог"
        id = request.form.get('vk_id')

        if not first_name or not surname or not date or not id:
            return render_template('horoscope.html', error="Пожалуйста, заполните все поля")

        cursor.execute('SELECT 1 FROM user_info WHERE vk_id=' + str(id) + ' LIMIT 1')
        if cursor.fetchone():
            return render_template('horoscope.html', error="Вы уже подписаны на рассылку")

        cursor.execute('INSERT INTO user_info (first_name, surname, bday, bmonth, zodiac_sign, vk_id) VALUES (%s, %s, %s, %s, %s, %s);',
                       (str(first_name), str(surname), int(bday), int(bmonth), str(zodiac_sign), int(id)))
        conn.commit()
        return render_template('horoscope.html', confirmation="Поздравляем! Вы подписались на рассылку")

    return render_template('horoscope.html')
