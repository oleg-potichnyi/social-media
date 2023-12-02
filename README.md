# Social media Project

This social media project is a web application that allows users to create accounts, share posts, manage their profiles, and schedule post creation with integration of Celery for background task scheduling.

## Features

* User-Centric Social Platform
* Scheduled Post Publishing
* RESTful API Integration
* Secure and Scalable
* Real-Time User Engagement

## Technology stack

* Backend:
  - Language: Python 3 
  - Framework: Django 
  - Database: Postgresql 
* Dependency Management: pip
* Virtual Environment: venv
* Database Migrations: Django Migrations
* Collaboration and Version Control:
  - Version Control System: Git
  - Repository Hosting: GitHub
* API Documentation: Swagger
* Task Queue: Celery
  - Message Broker: Redis
  - Monitoring Tool: Flower
* Authentication:
  - Framework: Django Authentication
  - Token-based: JWT
* Environment Variables: .env
* Other: requirements.txt

## Environment Variables

This project uses environment variables for sensitive information and configuration. Two files, `.env` and `.env_sample`, are provided:

- `.env_sample` serves as a template with variable descriptions.
- Create a copy of `.env_sample` and name it `.env` to set your environment-specific configuration.
- Fill in the values for each variable in `.env`.
- Keep `.env` secure and add it to your `.gitignore` to prevent accidental commits.

Never commit the `.env` file to your version control system.

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
