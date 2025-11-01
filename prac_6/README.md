# Dogs viewer

## Установка:

1. Клонируйте репозиторий  
2. Создайте виртуальное окружение и активируйте его  
3. Установите зависимости:  
   ```bash
   pip install -r requirements.txt
   ```
4. Создайте .env на основе примера:
    ```
    SECRET_KEY='ваш_ключ'
    ```
5. Выполните миграции:  
    ```bash
    python manage.py migrate
    ```
6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```




