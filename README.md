# 🎞️ MovieLanguage
(Openclassrooms) Project 13 : Create a project from scratch, to use the acquired knowledge on an opened subject.

This app contains quizzes about movies and series to improve your English.

### Installation and configuration 💻
- Create and activate virtual environment : `pipenv shell`
- Install packages with pipenv : `pipenv install`
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv`

**Clone the repository from Github by running this command:**

`git clone https://github.com/Lamia7/MovieLanguage.git`

**Execute with a virtual environment:**
Create a virtual environment: `pipenv shell` <br>
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` <br>
Activate the virtual environment: `pipenv shell` or `source venv/bin/activate` <br>
First time: install dependencies : `pipenv install` or `pip3 install requirements.txt`

Run the application: `python3 manage.py runserver` and go to your localhost : `http://127.0.0.1:8000/`

(To deactivate the virtual environment, run this command: `exit`)

### Features 📋
+ 

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


### Tests 🧪
- Launches the unit tests : `coverage run --source='.' manage.py test`
- Display the coverage report : `coverage report`
- Display the html coverage report details : `coverage html`


### Ressources used to create this program 🔧
***BACK***
- Language : Python 3.9
- Framework : Django 3.2

***DATABASE***
- ...

***FRONT***
- HTML5, CSS3
- Bootstrap 5
- Bootstrap5 template pack for django-crispy-forms library

### Author 📝
[Lamia EL RALIMI](https://github.com/Lamia7)