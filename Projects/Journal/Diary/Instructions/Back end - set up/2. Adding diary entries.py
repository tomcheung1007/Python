# Steps taken to create diary
# ADDING ENTRIES TO THE BACK END


# CONNECT ENTRIES APP TO DJANGO
# diary/settings.py >> add "entries.apps.EntriesConfig", to INSTALLED_APPS
# By adding entries.apps.EntriesConfig. It creates a connection between Django and entries.
# This allows Django to find its configurations for later use


# CREATE ENTRIES MODEL
# During the setting up stage, you created a database to store our diary entries.
# Next is to define database table where entries will be stored and how it is formatted
# see models.py


# REGISTER ENTRY MODEL TO DJANGO
# allows you to see entry model in Django admin site
# see entries/admin.py

# ______________________________________
# **CHECKPOINT**
# You have made the connection of our entries app to Django.
# You have also defined what info is stored via entries/models
# ______________________________________


# MIGRATE ENTRY MODEL
# terminal >> python manage.py makemigrations
# terminal >> python manage.py migrate
# makemigrations create migration files which contain Django instructions for building a database
# migrate implements them

# now when visiting the Django admin site, entries can be added into back end.
# next stage is to work on the front end

# ______________________________________
# **SUMMARY**
# You now have a functional back end where you can add and store entries
# Next is to create a front end where you can create, read, update, delete entries
# ______________________________________

