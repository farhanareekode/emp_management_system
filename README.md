# emp_management_system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend Will run at:
http://127.0.0.1:8000

Frontend
cd frontend
python -m http.server 5500
http://127.0.0.1:5500/index.html


