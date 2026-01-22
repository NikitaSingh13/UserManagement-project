# UserManagement — Django + DRF API

A simple, user management REST API built with Django and Django REST Framework. It provides CRUD operations for a custom `User` model with unique email validation and clean router-based URLs.

## Overview
- Frameworks: Django, Django REST Framework
- App: `users` with `User` model: `username`, `email`, `first_name`, `last_name`, `date_joined`
- API Base Path: `/api/`
- Database: SQLite (default; configurable)

## Project Structure
```
UserManagement/
	db.sqlite3
	manage.py
	UserManagement/
		settings.py
		urls.py
	users/
		models.py
		serializers.py
		views.py
		urls.py
```

## Requirements
- Python 3.10+
- Pip

Python deps are listed in [requirements.txt](requirements.txt):
- django
- djangorestframework

## Quick Start (Windows)
1) Create and activate a virtual environment
```
python -m venv venv
./venv/Scripts/Activate
```

2) Install dependencies
```
pip install -r requirements.txt
```

3) Apply migrations and run
```
cd UserManagement
python manage.py migrate
python manage.py runserver
```

Server starts at http://127.0.0.1:8000/
``



## API
Router is mounted at `/api/` in [UserManagement/UserManagement/urls.py](UserManagement/UserManagement/urls.py). The `users` endpoints are defined via a `DefaultRouter` in [UserManagement/users/urls.py](UserManagement/users/urls.py) and served by `UserViewSet` in [UserManagement/users/views.py](UserManagement/users/views.py).

Model and serializer:
- Model: [UserManagement/users/models.py](UserManagement/users/models.py)
- Serializer: [UserManagement/users/serializers.py](UserManagement/users/serializers.py) (validates unique `email`)

### Endpoints
- GET `/api/users/`: List users
- POST `/api/users/`: Create user
- PUT `/api/users/{id}/`: Replace user
- DELETE `/api/users/{id}/`: Delete user

### Request/Response Examples
Create a user
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
	-H "Content-Type: application/json" \
	-d '{
		"username": "jdoe",
		"email": "jdoe@example.com",
		"first_name": "John",
		"last_name": "Doe"
	}'
```

Sample response
```json
{
	"id": 1,
	"username": "jdoe",
	"email": "jdoe@example.com",
	"first_name": "John",
	"last_name": "Doe",
	"date_joined": "2026-01-22T12:34:56Z"
}
```

Validation errors (e.g., duplicate email) return DRF-style messages:
```json
{
	"email": ["Email already exists"]
}
```

## Running Tests
Add tests in [UserManagement/users/tests.py](UserManagement/users/tests.py) and run:
```powershell
cd UserManagement
python manage.py test
```

## Scaling & Production Notes
See detailed guidance in [SCALING_USERMANAGEMENT.md](SCALING_USERMANAGEMENT.md):
- Indexing, pagination, caching with Redis
- Asynchronous tasks with Celery
- Load balancing and horizontal scaling
- Serializer and queryset efficiency


