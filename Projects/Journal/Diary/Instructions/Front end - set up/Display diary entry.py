# Steps taken to create diary

# Frontend work. To display Diary as if you're the user and not admin

# CREATE LIST AND DETAIL VIEWS
# see entries/views.py
# There are two kinds of views, function based and class based views. In this project, we use class based views
# Django comes with generic views. This is utilised by making subclasses of DetailView and ListView

# CREATE TEMPLATES
# terminal >> mkdir -p entries/templates/entries
# see entries/templates/entries/entry_list.html
# see entries/templates/entries/entry_detail.html
# Here, templates folder is set up. It is set up in said way to make sure Django will find the right templates

# ADD ROUTES TO YOUR VIEWS
# see entries/urls.py
# see diary/urls.py
# To see templates in action, the views need to be connected to URLs.
# Then connect entries URLs to diary URLs

