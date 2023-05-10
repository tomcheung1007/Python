# Steps taken to create diary
# MANAGING OUR DIARY ON THE FRONT END - USER EXPERIENCE


# with web apps, there are four essential operations referred to as CRUD
# (C)reate, (R)ead, (U)pdate, (D)elete

# **CHECKPOINT**
# similar to before when setting up the ability to list and read entries.
# you will do the same for the other CRUD features
# 1. add views. 2. create templates and extend to base (PARENT) template. 3. Create URLs

# ADD VIEWS
# see entries/views.py
# previously you added ListView and DetailView to entries/views.
# Now it is time to add CreateView, UpdateView and DeleteView


# CREATE TEMPLATES
# see entries/template/entries/entry_confirm_delete.html
# see entries/template/entries/entry_form.html
# template for UpdateView is not required because entry_form will be used instead
# when entry_form is loaded, the form will be empty.
# when UpdateView is loaded, the form will be prefilled with title and content


# CREATE URLS
# see entries/urls


# **SUMMARY**
# you can now create, read, update and delete entries directly in the front end.
# overall, the same process was required:
# 1. add views
# 2. create templates and extend to base (PARENT) template
# 3. create URLs
