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

### Manage static directory 🖌️
``npm run build`` builds the project - this builds assets, HTML, JS, and CSS into dist\
``npm start`` or npm run start runs the project, launches a live preview in your default browser, and watches for changes made to files in src \
``npm run build:scss`` compiles the SCSS files located in the src/scss/ directory into dist \
``npm run build:assets`` copies the files in the src/assets/ directory into dist \
``npm run build:pug`` compiles the Pug located in the src/pug/ directory into dist \
``npm run build:scripts`` brings the src/js/scripts.js file into dist \
``npm run clean`` deletes the dist directory to prepare for rebuilding the project \
``npm run start:debug`` runs the project in debug mode



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