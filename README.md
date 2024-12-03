# Бекенд для сайта бронирования отелей | [English](#English)

Содержание

• [Описание](#Описание)

• [Функционал](#Функционал)

• [Технологии](#Технологии)

• [Установка](#Установка)

• [Тесты](#Тесты)

## Описание

Данный проект представляет собой API, разработанное с использованием FastAPI, которое предоставляет основные функции для системы бронирования отелей, включая регистрацию пользователей, логин, получение списка доступных отелей и создание бронирований и т.д. Также в проекте имеется простая фронтенд-страница, которая отображает список отелей.

Проект будет постоянно дополняться и улучшаться по мере изучения новых методов и технологий. Я планирую добавлять новые функции, такие как:

• Возможность фильтрации и сортировки отелей по различным параметрам (цене, рейтингу и т.д.)

• Расширенные возможности управления пользователями и их профилями

• Улучшение интерфейса фронтенда для более удобного взаимодействия

• Фронтенд

## Функционал

• Поиск отелей по различным параметрам (местоположение, дата)

• Система отзывов

• Создание, получение и удаление бронирований

• Управление пользователями (регистрация, авторизация Oauth2)

• Просмотр доступных номеров

• Загрузка картинок для отелей

• Импорт CSV файлов для добавления их в БД

• Тестирование Granfa + Prometheus

• Интеграция с платежными системами для обработки транзакций

## Технологии

• Язык программирования: [Python]

• Фреймворк: [FastAPI]

• База данных: [PostgreSQL]

• Другие технологии: [Redis, Docker, Granfa, Prometheus, Pytest, Alembic, Flake8]

• Фронтенд: [HTML]

## Установка

Клонируйте репозиторий:

```
git clone https://github.com/Rerotsu/Booking-Hotels-Backend.git
```

Перейдите в директорию проекта:

```
cd Booking-Hotels-Backend
```
Установка пакетов

```
pip install -r requirements.txt
```

Для создания и запуска образа используйте

```
docker comopse up --build
```
далее бекенд будет на http://localhost:7777/
для перехода в API: http://localhost:7777/docs/

## Тесты

### ВАЖНО!!!

ДЛЯ ТЕСТИРОВАНИЯ API РЕКОМЕНДУЕТСЯ ИСПОЛЬЗОВАТЬ СЕРВИС ДЛЯ ТЕСТИРОВАНИ API, К ПРИМЕРУ POSTMAN
ТОКЕН ПОЛЬЗОВАТЕЛЯ, ФОРМАТА Authorization Header, ДОЛЖЕН ПЕРЕДОВАТЬСЯ В ЗАГОЛОВОК

### Инструкция к тестам

Сервис [Postman](https://www.postman.com/)
1. Создаете POST-запрос на логин по URL http://127.0.0.1:7777/v1/auth/register
   передача идет в формате key:value
   email:почта
   First_name:Иия
   Last_name:фамилия
   email:пароль

   вовзращается Null далее идет логин(п.2)
   
2. Создаете POST-запрос на логин по URL http://127.0.0.1:7777/v1/auth/login 
   передача идет в формате key:value
   username:почта
   password:пароль

   вам передается сообщение с токеном
   далее вы создаете запросы, вставляя в keys 'Athourization header', а в Value ' {токен} bearer ' 
   
# English

## Contents

• [Description](#Description)

• [Features](#Features)

• [Technologies](#Tecnologies)

• [Installation](#Installation)

• [Testing](#Testing)

## Description

This project is an API developed using FastAPI, providing essential functions for a hotel booking system, including user registration, login, retrieving a list of available hotels, and creating bookings, among others. Additionally, the project includes a simple frontend page that displays the list of hotels.

The project will be continually enhanced and improved as I learn new methods and technologies. I plan to add new features such as:

• The ability to filter and sort hotels by various parameters (price, rating, etc.)

• Extended user management features and profiles

• Improvement of the frontend interface for more user-friendly interaction

• Frontend enhancements

## Features

• Search for hotels by various parameters (location, date, etc.)

• Create, retrieve, and delete bookings

• User management (registration, authorization)

• View available rooms

• Feedback system

• Upload images for hotels

• Import CSV files to add data to the database

• Testing with Granfa + Prometheus

• Integration with payment systems for transaction processing
## Technologies

• Programming Language: [Python]

• Framework: [FastAPI]

• Database: [PostgreSQL]

• Other Technologies: [Redis, Docker, Granfa, Prometheus, Pytest, Alembic, Flake8]

• Frontend: [HTML]

## Installation

Clone the repository:
```

git clone https://github.com/Rerotsu/Booking-Hotels-Backend.git

```

Navigate to the project directory:

```
cd Booking-Hotels-Backend
```

download packeges:

```
pip install -r requirements.txt
```

for create and start images use:

```
docker comopse up --build
```
Backend part will be locate at http://localhost:7777/
to switch to the API: http://localhost:7777/docs/

## Testing

### IMPORTANT!!!

TO TEST THE API, IT IS RECOMMENDED TO USE THE API TESTING SERVICE, FOR EXAMPLE POSTMAN
THE USER'S TOKEN, IN THE Authorization Header FORMAT, MUST BE TRANSFERRED TO THE HEADER

### Instructions for the tests

Service [Postman](https://www.postman.com)
1. Create a POST request for login by URL http://127.0.0.1:7777/v1/auth/register the
transfer is in the key format:value
 email:mail
 First_name:first name
 Last_name:last name
email:password

 Null is returned, followed by the login (item 2)

2. Create a POST request for login by URL http://127.0.0.1:7777/v1/auth/login 
 the transfer is in the key format:value
 username:mail
 password:password

 a message with a token
is sent to you, then you create requests by inserting an 'Athourization header' into keys, and 'Value' {token} bearer '
