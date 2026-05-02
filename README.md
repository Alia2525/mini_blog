Mini Blog API (FastAPI)

Невеликий REST API сервіс для публікації новин (Mini-Blog), реалізований на FastAPI з використанням JWT авторизації, ролей користувачів та SQLite бази даних.

---

Можливості

Користувачі

- Реєстрація
- Логін (JWT токен)
- Ролі:
  - user
  - moderator

Пости (Новини)

- Перегляд доступний всім
- Створення — тільки авторизовані
- Видалення:
  - автор
  - або moderator

Коментарі

- Перегляд — всім
- Створення — авторизовані

---

Технології

- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)

---

Встановлення

pip install -r requirements.txt

---

Запуск

uvicorn main:app --reload

---

API Документація

Після запуску відкрий:

http://127.0.0.1:8000/docs

Swagger UI дозволяє тестувати API прямо з браузера.

---

Авторизація

1. Зареєструйся:
   POST /register

2. Увійди:
   POST /login

3. Отримай токен:
   {
   "access_token": "..."
   }

4. Натисни Authorize в Swagger і встав:

Bearer ТВОЙ_ТОКЕН

---

Основні endpoints

Users

- POST /register
- POST /login

Posts

- GET /posts/
- POST /posts/
- DELETE /posts/{id}

Comments

- POST /comments/{post_id}

---

Права доступу

Дія| User| Moderator
Створення поста| так| так
Видалення свого поста| так| так
Видалення чужого поста| ні| так
Коментарі| так| так

---

Важливо

- Паролі зберігаються у вигляді hash (bcrypt)
- Використовується JWT для безпеки
- SQLite працює з check_same_thread=False

