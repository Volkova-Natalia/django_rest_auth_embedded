# django_rest_auth_embedded  
Packaged rest application to work with django embedded authentication.  

<br>

## Install the application  
The application **is not published**, so you should use link to the github repository:  
```shell script
pip install https://github.com/Volkova-Natalia/django_rest_auth_embedded/raw/master/dist/django_rest_auth_embedded-0.1.tar.gz
```

<br>

Edit your **settings.py** file to include 'django_rest_auth_embedded' in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_embedded',
]
```

<br>

And specify a custom user model from the application as the default user model for your project using the **AUTH_USER_MODEL** setting in your **settings.py**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_embedded.User'
```

<br>

Edit your project **urls.py** file to import the URLs:  
```python
urlpatterns = [
    ...
    path('auth/', include('django_rest_auth_embedded.urls')),
]
```

<br>

Finally, add the models to your database:  
```shell script
./manage.py makemigrations django_rest_auth_embedded
```  

<br>

## More information about the application  
The application realizes django embedded authentication.   
It is REST application. There are not templates.  

The application uses the following endpoints:  
***/registration/***  
***/login/***  
***/logout/***  
***/auth-info/*** - to check, the user is authenticated or not  
***/swagger/expected/*** - OpenApi specification of the application  

More information about the endpoints see ***/swagger/expected/***  
