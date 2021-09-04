# 🎞️ MovieLanguage
(Openclassrooms) Project 13 : Create a project from scratch, to use the acquired knowledge on an opened subject.

This app contains quizzes about movies to improve your English.

## Features 📋
+ Authentication
+ Display list of available quizzes
+ Choose a quizz
+ Reply to the questions
+ Display the result after you submit your answers
<hr>

## Installation and configuration 💻
- Create and activate virtual environment : `pipenv shell`
- Install packages with pipenv : `pipenv install`
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv`

**Clone the repository from Github by running this command:**

`git clone https://github.com/Lamia7/MovieLanguage.git`

**Execute with a virtual environment:** \
Create a virtual environment: `pipenv shell` \
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` \
Activate the virtual environment: `pipenv shell` or `source venv/bin/activate` \
First time: install dependencies : `pipenv install` or `pip3 install requirements.txt`

Run the application: `python3 manage.py runserver` and open your browser on your localhost address : `http://127.0.0.1:8000/`

(To deactivate the virtual environment, run this command: `exit`)

**Create a ``.env`` file that contains environmet variables:**

```
SECRET_KEY="your_secret_key"
ENV="your_environment_development_or_production"

DB_NAME="your_database_name"
DB_USER="your_database_user"
DB_PASSWORD="your_database_password"
PORT=your_database_port
```

Optional : you can also add this to the `.env` file:

```
SENTRY="your_dsn"
```
<hr>

### Checklist 📝
- [x] Download postgreSQL, added django + psycopg2-binary + libpq-dev
- [x] Initialize django project
- [x] Modify default settings
- [x] Create templates folder for templates organization
- [x] Create base.html template
- [x] Create the quizz app
- [x] Create home.html (CBV TemplateView) template and view
- [x] Create users app
- [x] Create register.html template and view + test
- [x] Test users models
- [x] Create login.html template with Django CBV
- [x] Create account.html template + view + test
- [x] Create logout.html template with Django CBV
- [x] Create quizz_list.html template + view + test
- [x] Create quizz models + test
- [x] Create quizz_list view (CBV ListView) + template
- [x] Create quizz view (CBV DetailView) + template
- [x] Create customized command to feed database + test
- [x] Create customized command to clear database + test
- [x] Create result view + template
- [ ] result test
- [x] Create legal_notice.html (CBV TemplateView) template and view
- [ ] Create password reset feature (views, templates and tests)
<hr>

## Tests 🧪
- Launches the unit tests : `coverage run --source='.' manage.py test`
- Display the coverage report : `coverage report`
- Display the html coverage report details : `coverage html`
<hr>

## Ressources used to create this program 🔧
***BACK***
- Language : Python 3.9
- Framework : Django 3.2

***DATABASE***
- PostgreSQL

***FRONT***
- HTML5, CSS3
- Bootstrap 5
- Bootstrap5 template pack for django-crispy-forms library
- Sass

***EXTERNAL RESSOURCES***
- Web server /  HTTP server : [Nginx](https://www.nginx.com/)
- HTTP/WSGI server : [Gunicorn](https://gunicorn.org/)
<hr>

## Author 📝
[Lamia EL RALIMI](https://github.com/Lamia7)