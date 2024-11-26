# Backend for Hotel Booking Website | Бекенд для сайта бронирования отелей

## Contents | Содержание

- [Description | Описание](#description)
- [Features | Функционал](#features)
- [Technologies | Технологии](#technologies)
- [Installation | Установка](#installation)
- [Testing | Тесты](#testing)

## Description

This project is an API developed using FastAPI, providing essential functions for a hotel booking system, including user registration, login, retrieving a list of available hotels, and creating bookings, among others. Additionally, the project includes a simple frontend page that displays the list of hotels.

The project will be continually enhanced and improved as I learn new methods and technologies. I plan to add new features such as:

*Данный проект представляет собой API, разработанное с использованием FastAPI, которое предоставляет основные функции для системы бронирования отелей [регистрация пользователей, логин, получение списка доступных отелей и создание бронирований и тд].
Так же, в проекте имеется простая фронтенд-страница, которая отображает список отелей.*

*Проект будет постоянно дополняться и улучшаться по мере изучения новых методов и технологий. 
Я планирую добавлять новые функции, такие как:*

- The ability to filter and sort hotels by various parameters (price, rating, etc.) | *Возможность фильтрации и сортировки отелей по различным параметрам (цене, рейтингу и т.д.)*
- Integration with payment systems for transaction processing | *Интеграция с платежными системами для обработки транзакций*
- Extended user management features and profiles | *Расширенные возможности управления пользователями и их профилями*
- Improvement of the frontend interface for more user-friendly interaction | Улучшение интерфейса фронтенда для более удобного взаимодействия
- Frontend enhancements | Фронтенд

## Features

- Search for hotels by various parameters (location, date, etc.) | *Поиск отелей по различным параметрам (местоположение, дата)*
- Create, retrieve, and delete bookings | *Создание, получение и удаление бронирований*
- User management (registration, authorization) | *Управление пользователями (регистрация, авторизация)*
- View available rooms | *Просмотр доступных номеров*
- Upload images for hotels | *загрузка картинок для отелей*
- Import CSV files to add data to the database | *импорт csv файлов для добавления их в БД*
- Testing with Granfa + Prometheus | *Тестирование Granfa + Prometheus*

## Technologies

- Programming Language: [Python]
- Framework: [FastAPI]
- Database: [PostgreSQL]
- Other Technologies: [Redis, Docker, Granfa, Prometheus,Pytest, Alembic, Flake8]
- Frontend: [HTML]

## Installation

Clone the repository: | Клонируйте репозиторий
```
git clone https://github.com/Rerotsu/Booking-Hotels-Backend.git
```

Navigate to the project directory: | *Перейдите в директорию проекта*

```
cd Booking-Hotels-Backend

pip install -r requirements.txt
```

## Testing

Instructions for running tests.

The project uses pytest for testing. To run the tests, use:

*Инструкции по запуску тестов.*

*в проекте осуществляются тесты с помощью pytest
для запуска теста используется:*

```
pytest
``` 


