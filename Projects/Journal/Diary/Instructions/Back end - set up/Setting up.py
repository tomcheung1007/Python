# Steps taken to create diary

# SET UP VIRTUAL ENVIRONMENT
# file >> New project

# INSTALL DJANGO
# terminal >> pip install Django==3.2.1

# INITIALISE DJANGO terminal >> django-admin startproject diary .  (IMPORTANT -  . prevents Django from creating another
# directory for your diary project.)
# Initialising Django will create a number of files

# CREATE THE DATABASE - to store content of diary
# terminal >> python manage.py migrate

# CREATE SUPERUSER
# terminal >> python manage.py createsuperuser

# RUN DEVELOPMENT WEB SERVER - The home page of diary
# terminal >> python manage.py runserver
# IMPORTANT - must run web server first before visiting diary in browser

