create venv: python3 -m venv attendance-env

activate venv: source attendance-env/bin/activate

install requirements: pip install -r requirements.txt

run migrations: python manage.py migrate

run server: python manage.py runserver

