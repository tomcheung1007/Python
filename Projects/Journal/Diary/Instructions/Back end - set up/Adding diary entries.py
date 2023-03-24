# Steps taken to create diary

# SET UP APP FOR ENTRIES
# terminal >> python manage.py startapp entries
# this creates an entries folder within your project with predefined files.

# CONNECT ENTRIES APP TO DJANGY PROJECT
# diary/settings.py >> add "entries.apps.EntriesConfig", to INSTALLED_APPS

# CREATE ENTRIES MODEL
# defining database table where entries will be stored
# see models.py

# REGISTER ENTRY MODEL
# allows you to see entry model in Django admin site

# MIGRATE ENTRY MODEL
# terminal >> python manage.py makemigrations
# terminal >> python manage.py migrate

# now when visiting the Django admin site, entries can be added into back end.
# next stage is to work on the front end

