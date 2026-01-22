# UserManagement — Django + DRF API

A simple, user management REST API built with Django and Django REST Framework. It provides CRUD operations for a custom `User` model with unique email validation and clean router-based URLs.

## How to Use the API

The application exposes REST APIs using Django REST Framework. The APIs can be accessed via the live deployment URL.

### Base URL
https://usermanagement-project-y6g9.onrender.com/

### 1. API Root
To view available API endpoints:
https://usermanagement-project-y6g9.onrender.com/api/

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

All API endpoints are exposed under the `/api/` path.

The API routing is configured using Django REST Framework **ViewSets and Routers** to ensure clean and scalable endpoint management.

- The main API router is mounted at `/api/` in  
  `UserManagement/UserManagement/urls.py`.
- The `users` endpoints are registered using a `DefaultRouter` in  
  `UserManagement/users/urls.py`.
- All user-related API logic is handled by the `UserViewSet` defined in  
  `UserManagement/users/views.py`.

### Model and Serializer

- **User Model**:  
  Defined in `UserManagement/users/models.py`.  
  It includes fields such as `username`, `email`, `first_name`, `last_name`, and `date_joined`.

- **User Serializer**:  
  Implemented in `UserManagement/users/serializers.py`.  
  The serializer is responsible for serializing and deserializing user data and includes field-level validation, such as enforcing the uniqueness of the `email` field.


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
		"username": "Nikita",
        "email": "nikitasinghak257@gmail.com",
        "first_name": "Nikita",
        "last_name": "Kumari",
	}'
```

Sample response
```json
{
	"id": 1,
	"username": "Nikita",
	"email": "nikitasinghak257@gmail.com",
	"first_name": "Nikita",
	"last_name": "Kumari",
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


