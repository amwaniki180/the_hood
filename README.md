# Neighborhood

 This is a Django-based web app that makes it easier people living within the same neighbourhood to keep tabs on each other.

#### By ANTONY MWANIKI


## Behavior Driven Development (BDD)
| General Behavior | Input    | Output   |
| :------------- | :------------- | :------------- |
| User is authenticated | On homepage, click the sign up button  | Redirected to the user registration page |
| User can edit/add their profile details | Clicks edit profile button  | Redirected to the profile page form template |
| User can join a neighborhood | Clicks on the neighborhood image  | Redirected to the profile's page to fill required details |
| User can search for specific business | Type the business name on the search bar | Redirected to the results-page |
| User can update their neighborhood  | User clicks their profile to edit details | the change is updated |
| User can create a post  | Create a post | The post is displayed in the neighbourhood the user is in |

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE HOOD;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'HOOD'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

```
### Run initial Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the app
```bash
python manage.py runserver
```
Open terminal on `localhost:8000`


## Technologies used
    - Python 3.7
    - HTML
    - Bootstrap 4
    - JavaScript
    - Django
    - Heroku
    - Postgresql

## Support and contact details
Contact me on dmwaigithinji@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **ANTONY MWANIKI**