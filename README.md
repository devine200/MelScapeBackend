# MELSCAPE PROPERTY MANAGEMENT AGENCY

This is a fullstack property management website for our client MelScape property management Agency based out of the UK.

At MelScape, we handle every aspect of property management, from marketing and listing to maintenance and guest communication.

We ensure that properties are well-maintained, secure, and operating efficiently, taking the hassle out of managing rental properties for owners.

### TECHNOLOGY STACK
This project is written with HTML, CSS and JavaScript on the frontend.


Django Framework was used for the backend as well as Jinja template engine.

## PROJECT SETUP

### CLONE PROJECT
```bash
git clone https://github.com/devine200/MelScapeBackend.git
```


### CREATE & SETUP VIRTUAL ENVIRONMENT

#### INSTALL VIRTUALENV
```bash
pip install virtualenv
```

#### ACTIVATE VIRTUALENV
```bash
virtualenv env && source env/bin/activate
```

#### INSTALL PROJECT DEPENDENCIES
```bash
pip install -r requirements.txt
```

### START UP PROJECT SERVER

#### CREATE DATABASE MIGRATIONS
```bash
python melscape_server/manage.py makemigrations && python melscape_server/manage.py migrate
```

#### START UP PROJECT SERVER
```bash
python melscape_server/manage.py runserver
```

You should be able to access the project at [http://localhost:8000](http://localhost:8000) by default
