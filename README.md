## My Django learning
# Intro
- Django is a python web framework
- Uses a concept known as object-relational mapping which makes working with databases easier

# Virtual Environment 
- Using venv(virtual environment)
- It is suggested to have a virtual environment when working with Django
- Installing python3.10-venv
- To start, first create a directory for the virtual environment
  python3 -m venv 'name_of_directory'
- Then activate with
  source name_of_directory/bin/activate

# Setting up Django
- Installing Django to your computer
- Command: python3 -m pip install Django

# Starting project
- Once you pick a suitable name for your Django project, navigate where you want to store your code
- Run: django-admin startproject my_tennis_club
- Run: python3 manage.py runserver
- To see it your project has been setup correctly

# The MANAGE.PY file
- This script is a central command-line utility that is automatically created when you generate a new Django project.
- It plays a critical role in Django development
- offers administrative and management tasks for your Django project
- Purpose: Acts as an entry poitn for your Django project
         : Provides (CLI) to interact with the project, allowing you to perform tasks
         : Tasks such as, running dev server, migrating the database, creating new apps.

# Creating Apps
- An app is a web application that has a specific meaning to your project, like homepage, a contact form, or a members database
- In this tutorial, we will create an app that allows us to list and register members in a database

# THE (views.py) FILE
- Django views are python functions that take http request sand returns http response
- A web page that uses Django is full of views with different tasks and missions- Views are usually put in a file called views.py

# THE (urls.py) FILE
- The urls.py file is created manually for the specific app within the django project
- There are two urls.py file
- The route urls.py, found inside the project folder(That is created automatically once you start django project)
- The app urls.py, this is created manually inside the app

# TEMPLATES
- Django templates result should be in html
- And it should be created in a template
- It should be as a folder named templates inside the app folder
- After creating the html file inside the template folder
- modify the views.py file importing loader
- In the settings.py file add the members app inside the list of installed apps

# MODELS
- Here we will see how Django works with data
- In Django, data is created in objects, called model  and is actually tables in a database
- Models are found in the models.py file
- When we created the Django project, we got an empty SQLite database
- By default, all Models created in the Django project will be created as tables in this Database
- When you define/describe a Model in the models.py file, you must run a command to actually create a table in the database
- Run: python3 manage.py makemigrations members

# DJANGO Insert Data
- We use the python interpreter(Python shell) to add some members to it
- Run: python3 manage.py shell





