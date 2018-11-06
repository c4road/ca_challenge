# Reviews API

## Requirements

The main requirements are:

- Python 3.6+
- Django Django==2.1.2
- Django Rest Framework 3.9.0
- Postman

You can see the other requirements inside the requirements files.

## Installing

First you need to activate the environment.

On windows:
```bash
virtualenv env
env\Scripts\activate
```

On linux:
```bash
virtualenv env
source env/bin/activate
```

To install this project you can use `pip` or download individually which library from PyPI.

Using `pip`, you can run the following commands for each environment you want.

```bash
pip install -r requirements.txt
```

## Setting Up

The environment is using SQLite by default, to make easier to run and test the project. 

After setup the DB, you need to run the following commands to have the data scheme right.

```bash
python manage.py makemigrations authentication reviews companies
python manage.py migrate
python manage.py createsuperuser
```

There you will be prompted to enter the superuser credentials: username, email
and password.

## Loading initial data

To load some data into the database you must run the following commands. Being located in the root of the project

```bash
python manage.py loaddata companies.json
python manage.py loaddata reviewers.json
python manage.py loaddata reviews.json
```

## Running

To run this project, you can just run the following command:

```bash
python manage.py runserver
```

This command will run the project in `development` mode.

You can access the admin page by `http://localhost:8000/admin` and using the previous created superuser. 
Then, you can manage the users and their access tokens.

## Testing


To run all the tests, you run the following command:

```bash
python manage.py test
```

## Code coverage


To run all the tests, you run the following commands:

```bash
coverage run --source='authentication','companies','reviews' manage.py test
coverage report
```

## Modeling Design

1) In this challenge I used JSON Web Token instead of DRF Token because nowadays it is considered an standard. Here you can see an answer that explain the difference between eachetter. https://goo.gl/t9ayqA

3) The architecture is based the style guide and reference book Two Scoop of DJango 2.

2) Ip address is taken for the request object but It could be also fetched by the frontend.

4) Core module is used basically to implement DRY

5) Reviewers is a custom user module that provides both authentication and review metadata. In broader circumstances is useful separating those concerns and implement some third party package for authentication like djoser https://goo.gl/q8rMHy

6) I assumed that when reviewing the user is in a company detail view, and thats why I take the company id from url kwargs when creating a review. Considering default viewset create endpoint doesnt use url kwargs, thats why I used generic CreateAPIView instead of Viewset. Nevertheless, I use viewsets in companies module. 

7) I inherited from three types of django rest framework views to demonstrate a broader skillset

8) I used custom json renderers to allow custom labels in singular and plural form.


## API documentation

To take a look at the api endpoints I recommend using Postman. You have to import the API.postman_collection.json and API.postman_environment.json, also you can visit http://localhost:8000/swagger/, http://localhost:8000/redoc/, and http://localhost:8000/docs/ for further information.