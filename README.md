# Social media Project

This social media project is a web application that allows users to create accounts, share posts, manage their profiles, and schedule post creation with integration of Celery for background task scheduling.

## Features

* User-Centric Social Platform
* Scheduled Post Publishing
* RESTful API Integration
* Secure and Scalable
* Real-Time User Engagement

## Installation

Python3 must be already installed

```shell
- Сreate venv: "python3 -m venv venv"
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
- Install requirements: "pip install -r requirements.txt"
- Run migrations: "python manage.py migrate"
- Run Redis Server: "docker run -d -p 6379:6379 redis"
- Run celery worker for tasks handling: "celery -A social_media_api worker -l INFO"
- Run celery beat for tasks scheduling: "celery -A social_media_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"
- Run app: "python manage.py runserver"
```

## User credentials

```shell
Email: oleg@admin.com
password: admin12345
```
