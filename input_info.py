import psycopg2
from generation_of_horoscope import name, month, day, sign

conn = psycopg2.connect(database="stars",
                        user="postgres",
                        password=" ",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


def input_info():
    cursor.execute('SELECT 1 FROM user_info WHERE first_name=%s AND bday=%s AND bmonth=%s AND zodiac_sign=%s '
                   'LIMIT 1', (str(name), str(day), str(month), str(sign)))
    if cursor.fetchone():
        pass
    else:
        cursor.execute('INSERT INTO user_info (first_name, bday, bmonth, zodiac_sign) VALUES (%s, %s, %s, %s);',
                   (str(name), str(day), str(month), str(sign)))
        conn.commit()


input_info()
