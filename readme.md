# Project Attendace

## Description

Children living in homes across Japan are unmonitored for large parts of the day. 
Between traveling from home to school to school clubs to tutoring and back to home, staff, caregivers, and administrators often have no idea where the children are. 
Our goal will be to build a platform using a fingerprint hardware to keep track of the children's movements and ensure their safety.

## How to run:

1. Backend: go to backend folder (requires python 3)

Install python3 on your machine and make sure python points to python3 and pip points to pip 3, it is recommended to use venv for setting this

Run ```pip install -r requirements.txt```

run ```python manage.py migrate```

run ```python manage.py createsuperuser```

run ```python manage.py runserver```

backend should be available at localhost:8000 now

admin page url is localhost:8000/admin/

2. Frontend: go to frontend folder (requires nodeJs and yarn)

run ```yarn install```

run ```yarn start```

frontend will be available at localhost:3000

3. Simulator tool (to simulate minors moving between waypoints) go to tools/simulator folder

run ```yarn install```

run ```node index.js```

simulator will start send minorWaypointHistory messages to backend with random payload and interval



## Useful commands:

create venv: ```python3 -m venv attendance-env```

activate venv: ```source attendance-env/bin/activate```

install requirements: ```pip install -r requirements.txt```

save requirements to file: ```pip freeze > requirements.txt```

run migrations: ```python manage.py migrate```

run server: ```python manage.py runserver```

create superuser: ```python manage.py createsuperuser``` (default: root, iamroot123)

