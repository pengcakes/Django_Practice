References
- https://realpython.com/django-rest-framework-quick-start/
- https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

Model Serializer
- Serialization is the process of converting an object into bytes so you can
	store it or send it around
- in DRF, the Serializer converts models instances to Python Dicts
-	This way, they can be rendered into API usable formats such as JSON or XML


To-do list to create a REST API in Django
    Set up Django
    Create a model in the database that the Django ORM will manage
    Set up the Django REST Framework
    Serialize the model from step 2
    Create the URI endpoints to view the serialized data


Views vs Viewsets: https://stackoverflow.com/questions/32589087/difference-between-views-and-viewsets
	- Seems like viewsets are easier, only need to efine one pattern in urls.py 
