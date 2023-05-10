# Steps taken to create diary
# DISPLAYING ENTRIES ON THE FRONT END


# CREATE LIST AND DETAIL VIEWS
# see entries/views.py
# There are two kinds of views. function based and class based views. In this project, you use class based views
# Django comes with generic views. This is utilised by making subclasses of DetailView and ListView


# CREATE TEMPLATES
# terminal >> mkdir -p entries/templates/entries
# Here, templates folder is set up. It is set up in said way to make sure Django will find the right templates

# see entries/templates/entries/entry_list.html
# see entries/templates/entries/entry_detail.html
# these templates are coded in html and translates to what you see when viewing entries


# ______________________________________
# **CHECKPOINT**
# templates have been created that will allow you to list and view entries on the front end
# next step is to connect these to Django
# ______________________________________


# ADD ROUTES TO YOUR VIEWS
# see entries/urls.py
# note how it relates to entries/templates/entries to see how they connect

# see diary/urls.py
# this connects the entries/urls to the URLs that Django uses


# ______________________________________
# **SUMMARY**
# By creating templates and linking them to the diary URL,
# the entries you make in the backend are now visible from the front end
# ______________________________________



