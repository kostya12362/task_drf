# task_drf
Базовая документация
Регистрация пользователя

запрос POST
http://127.0.0.1:8000/api/v1/registration/
Body
| Key | Value |
|-:|-:|
| username | kostya12362 |
| password | ostapenko123 |
```json
{
    "id": 2,
    "username": "kostya12362"
}
```

POST
http://127.0.0.1:8000/api/v1/login/
Body
| Key | Value |
|-:|-:|
| username | kostya12362 |
| password | ostapenko123 |

Ответ
{
    "token": "a161c5b185e18306c6b4034c410449a2487855ea"
}

GET
http://127.0.0.1:8000/api/v1/event/
Headers
Key: Authorization VALUE: Token a161c5b185e18306c6b4034c410449a2487855ea

Ответ
[
    {
        "event_type": "11111",
        "info": {
            "1234": "3343"
        },
        "timestamp": "2011-09-01 16:20:30.000000"
    }
]

POST
http://127.0.0.1:8000/api/v1/event/
key event_type value create task
key info value {"task":"1"}
key timestamp value 2011-09-01 13:20:30
