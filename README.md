# Django Library Book Management App

A library application built with Django, Bootstrap, Python, and CSS.

## Project Screen Shots
<img src="https://github.com/chrisnumber49/DjangoLibraryApp/blob/master/screen%20shot/demo1.PNG" width="800" > 
<img src="https://github.com/chrisnumber49/DjangoLibraryApp/blob/master/screen%20shot/demo2.PNG" width="800" > 

## Installation and Setup Instructions

Clone down this repository. You will need `Django` installed globally on your machine.  

Installation: `pip install Django`

Creating new migrations: `python manage.py makemigrations`

Applying migrations: `python manage.py migrate`

To Start Server: `python manage.py runserver`  

To Visit App: `localhost:8000/`

## Reflection 
 
In this project, we can create, read, update, and delete the information of book objects in the database. I started this project by using the command `django-admin startproject` to create the boilerplate of the project, then create a new app with the command `python manage.py startapp`, dependency `pillow` was installed for saving and serving static files to the client.

Through this side project, I learned about how the CRUD operations perform with Django ORM (object-relational mapper) in the Django Views, the concept of ModelForm to quickly build CRUD with form data, and lastly the `csrf_token` in Django form security verification to prevent people to attack the website through form's data.
