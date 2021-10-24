Summary of Django files: https://dev.to/chrisdevcode/django-files-explained-1e05

PROJECT FILES - the whole thing
1. manage.py - cmd utility (not used)
2. __init__.py - lets Python know this is a Python package
3. setting.py - setting for Django project
4. urls.py - table of contents of your website
5. asgi.py + wsgi.py - entry point for asgi + wsgi servers

APP FILES - kind of like objects
1. admin.py - register models here to edit them on /admin
2. apps.py - config code for this APP goes here
3. models.py - models are tables used for storing data. They are defined here.


4. tests.py - tests are important
4. views.py - request handler (HTTPS), takes requests + sends responses. HTML templates are not really
used in Django but can be. There is an example templates folder included in the playground app.
