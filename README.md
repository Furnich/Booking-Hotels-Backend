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

• Интеграция с платежными системами для обработки транзакций

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

Инструкции по запуску тестов.

В проекте осуществляются тесты с помощью pytest. Для запуска теста используется:
```
pytest
```


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

• Integration with payment systems for transaction processing

• Extended user management features and profiles

• Improvement of the frontend interface for more user-friendly interaction

• Frontend enhancements

## Features

• Search for hotels by various parameters (location, date, etc.)

• Create, retrieve, and delete bookings

• User management (registration, authorization)

• View available rooms

• Upload images for hotels

• Import CSV files to add data to the database

• Testing with Granfa + Prometheus

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

Instructions for running tests.

The project uses pytest for testing. To run the tests, use:
```
pytest
```
