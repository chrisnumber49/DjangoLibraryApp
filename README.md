# Django Library App

An library application built with Django, Bootstrap, python, and CSS.

This application is deployed on: https://djangolibraryappchris49.herokuapp.com/

## Project Screen Shots
<img src="https://github.com/chrisnumber49/DjangoLibraryApp/blob/master/screen%20shot/demo1.PNG" width="600" > 
<img src="https://github.com/chrisnumber49/DjangoLibraryApp/blob/master/screen%20shot/demo2.PNG" width="600" > 

## Installation and Setup Instructions

Clone down this repository. You will need `django` installed globally on your machine.  

Installation: `pip install Django`

Creating new migrations: `python manage.py makemigrations`

Applying migrations: `python manage.py migrate`

To Start Server: `python manage.py runserver`  

To Visit App: `localhost:8000/`

## Reflection 

In this project we can create, read, update and delete the book object in the database. I started this project by using the command `django-admin startproject` to create the boilerplate of project, then create new app with command `python manage.py startapp`, dependency `pillow` were installed for saving and serving static files to the client.

Through this side project, I learned about the basic CRUD operations with Django ORM (object-relational mapper)
