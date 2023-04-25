# Steps taken to create diary

# SET UP APP FOR ENTRIES
# terminal >> python manage.py startapp entries
# this creates an entries folder within your project with predefined files.

# CONNECT ENTRIES APP TO DJANGO
# diary/settings.py >> add "entries.apps.EntriesConfig", to INSTALLED_APPS

# CREATE ENTRIES MODEL
# defining database table where entries will be stored and how it is formatted
# see models.py

# CONNECT ENTRY MODEL TO DJANGO
# allows you to see entry model in Django admin site
# see entries/admin.py

# MIGRATE ENTRY MODEL
# terminal >> python manage.py makemigrations
# terminal >> python manage.py migrate
# makemigrations create migration files which contain Django instructions for building a database
# migrate implements them

# now when visiting the Django admin site, entries can be added into back end.
# next stage is to work on the front end

