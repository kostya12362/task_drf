# task_drf

## Installation
```bash
$ pip install virtualenv
```

The next step is to create a directory in which our folder will be in the environment
```linux
$ mkdir dev_test && cd dev_test
$ git clone https://github.com/kostya12362/task_drf.git
$ cd task_drf
$ python3 -m venv venv
```
We activate the environment and run project
```linux
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver 127.0.0.1:8000
```
> if you want see test
```linux
$ coverage run --omit=*/venv/*,*/migrations/*,*/event/tests/* manage.py test event
$ coverage report
```

## Basic api documentation </br>

---

User registration

##### http://127.0.0.1:8000/api/v1/registration/ </br>
* POST <br/>

Body <br/>

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
---

##### http://127.0.0.1:8000/api/v1/login/ <br/>
* POST <br/>

Body <br/>

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
---

##### http://127.0.0.1:8000/api/v1/event/ <br/>
* GET <br/>

Headers <br/>

| Key | Value |
|-:|-:|
| Authorization | Token a161c5b185e18306c6b4034c410449a2487855ea |

Ответ <br/>
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

* POST <br/>

Headers <br/>

| Key | Value |
|-:|-:|
| Authorization | Token a161c5b185e18306c6b4034c410449a2487855ea |

Body <br/>

> If __event_type__ does not exist in the database, a new instance is created in the __EventType__ model

| Key | Value | Format |
|-:|-:|-|
| event_type | create task | string |
| info | {"task":"1"} | json |
| timestamp | 2011-09-01 13:20:30 | %Y-%m-%d %H:%M:%S.%f |

```json 
{
    "event_type": "create task",
    "info": {
        "task": "1"
    },
    "timestamp": "2011-09-01 13:20:30.000000"
}
```

