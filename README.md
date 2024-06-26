**Django Project**

Это веб-приложение на Django для учета успеваемости студентов. 

**Функционал:**

* Создание, просмотр, редактирование и удаление данных о студентах, предметах и оценках.
* Фильтрация и сортировка списка оценок.
* Отображение лучших и худших студентов по среднему баллу.
* Расчет средних баллов по предметам.

## Инструкции по запуску

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/dektor120/django_project.git
   ```

2. **Создайте виртуальное окружение:**

   ```bash
   python3 -m venv .venv
   ```

3. **Активируйте виртуальное окружение:**

   *  **Linux/macOS:**
      ```bash
      source .venv/bin/activate
      ```
   *  **Windows:**
      ```bash
      .venv\Scripts\activate
      ```

4. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Примените миграции базы данных:**

   ```bash
   python manage.py migrate
   ```

6. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   ```

7. **Откройте приложение в браузере:** http://127.0.0.1:8000/
