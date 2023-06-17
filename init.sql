CREATE DATABASE stars;
\c stars
CREATE TABLE user_info (id SERIAL PRIMARY KEY, first_name text NOT NULL, surname text, bday int NOT NULL, bmonth int NOT NULL, zodiac_sign text, vk_id integer, mail varchar);
