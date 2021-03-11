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
```json
{
    "token": "a161c5b185e18306c6b4034c410449a2487855ea"
}
```

GET
http://127.0.0.1:8000/api/v1/event/
Headers
| Key | Value |
|-:|-:|
| Authorization | Token a161c5b185e18306c6b4034c410449a2487855ea |

Ответ
```json
[
    {
        "event_type": "11111",
        "info": {
            "1234": "3343"
        },
        "timestamp": "2011-09-01 16:20:30.000000"
    }
]
```

POST
http://127.0.0.1:8000/api/v1/event/
Headers
| Key | Value |
|-:|-:|
| Authorization | Token a161c5b185e18306c6b4034c410449a2487855ea |
Body
| Key | Value | Format |
|-:|-:|-|
| event_type | create task | string |
| info | {"task":"1"} | json |
| timestamp | 2011-09-01 13:20:30 | %Y-%m-%d %H:%M:%S.%f |

