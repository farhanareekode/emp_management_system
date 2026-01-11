#  Emp Management System

A Django-based employee management system with JWT authentication.

---


This project has **two parts**:
- Backend (Django API)
- Frontend (Static HTML/CSS/JS)

Both must be running at the same time.

---

## Backend Setup (Django)

From the project root (where `manage.py` exists):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Frontend Setup 
cd frontend
python -m http.server 5500
http://127.0.0.1:5500/index.html
