# Home bot

# Установка
- Скопируйте проект
    ```console
    $ git clone
    ```
- Скопируйте `.env`, либо создайте руками
    ```console
    $ cp .env.example .env
    ```
- Установите параметры в файле `.env`
- Запустите контейнер
    ```console
    $ docker-compose up -d --build
    ```
  
# Разработка
## Миграции
- Создать миграции
    ```console
    $ alembic revision --message="Название" --autogenerate
    ```
- Поднять миграции
    ```console
    $ alembic upgrade head
    ```
- Откатить миграцию
    ```console
    $ alembic downgrade -1
    ```
