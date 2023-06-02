# Meta Back-end developer Certification End of API Course

## Setting virtual environment

$ pipenv install

$ pipenv //--> to check if your local environment already have pipenv

$ pipenv install django

$ django-admin startproject LittleLemon .

$ pipenv shell //--> activates the virtual environment

$ update dependencies on Pipfile

[packages]
django = "*"
djangorestframework = "*"
djangorestframework-xml = "*"
djoser = "*"

$ pipenv install  //--> updates the dependencies

$python manage.py startapp LittleLemonAPI

### Other commands

$ python manage.py runserver

$ python manage.py makemigrations //--> upload dataset from models.py 

$ python manage.py migrate //--> commit dataset to browser

## Setup DRF(Django Rest Framework)

$ pipenv install djangorestframework

## Setup Djoser for authentication

$ pipenv shell
$ pipenv install djoser

--> settings.py
INSTALLED_APPS = [
    'djoser'
]

DJOSER = {
    'USER_ID_FIELD':'username',
    'LOGIN_FIELD':'email', //--> to set username as email
}
## Additional applications needed in LittleLemonDRF

* urls.py
* serializers.py

# Project requirements

## Business need

* Create a fully functioning API project so that the client application develops can use the APIs to develop web and mobile application.  

* People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders

## Structure

* Create a single Django app called LittleLemonAPI in virtual environment

## Function or class-based views

* Choose class-based views for less code

## User groups

$ python manage.py createsuperuser

Username: admin
Password: password@1
Email: admin@littlelemon.com

* Manager
--edit menu and category, update roles, assign and filter
* Delivery crew
--browse order and mark orders

## Error check and proper status code

## API endpoints

* user registration and token generation endpoints

* Menu-items endpoints

* user group management endpoints

* cart management endpoints

* order management endpoints

## Additional steps

* implement filtering, sorting, searching, and pagination

## Throttling

