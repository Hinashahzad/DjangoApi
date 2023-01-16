# DjangoApi

## Introduction
Creating Backend using Python Framework Django

## Installation dependeancy

`pip install python`
`pip install django`
`pip install djangorestframework`
`django-admin startproject apiProject`

## Optional installation
`pip install markdown`       # Markdown support for the browsable API.
`pip install django-filter`

## Run the Server

`python manage.py runserver`

## ADD rest-framework inside the installed app in system.py

`INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest-framework"
]`

## Create Readonly add in the settings.py
`REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}`

## Create APP for creating the django api
`python manage.py startapp api`

## Create the MODEL by using the following command in terminal
`python manage.py makemigrations` 

## To reflects the changings into the database (Send data from MODEL to DATABASE ) use the following command in terminal
`python manage.py migrate`

## Install Postman 
1. GET   Get the APIs
   "[
    {
        "url": "http://127.0.0.1:8000/api/v1/products/1/",
        "name": "Bridal_lahnga",
        "about": "This is the bridal lehnga with heavy detailing all around the fabric",
        "product_description": "Color: Red, detailing: heavy dabka work",
        "type": "Western",
        "added_date": "2023-01-16T11:03:12.604868Z"
    },
    {
        "url": "http://127.0.0.1:8000/api/v1/products/2/",
        "name": "Bridal_Saree",
        "about": "This is the heavy embroidered Bridal Saree",
        "product_description": "Color: Royal Blue, heavily detailing on damman",
        "type": "Eastern",
        "added_date": "2023-01-16T11:27:17.827895Z"
    },
    {
        "url": "http://127.0.0.1:8000/api/v1/products/3/",
        "name": "Bridal Garara",
        "about": "This is the heavy embroidered Bridal Garara",
        "product_description": "Color: Orange, heavily detailing on front pannel",
        "type": "Eastern",
        "added_date": "2023-01-16T11:39:48.044836Z"
    }
]"
2. POST 
    '{
    "name": "Bridal Garara 2",
    "about": "This is the heavy embroidered Bridal Garara",
    "product_description": "Color: Orange, heavily detailing on front pannel",
    "type": "Eastern",
    "added_date": "2023-01-16T12:27:17.827895Z"
}'
3. PUT
    ' {
        "name": "Bridal_lahnga",
        "about": "This is the bridal lehnga with heavy detailing all around the fabric",
        "product_description": "Color: Pink, detailing: heavy dabka work and thread work on back",
        "type": "Western",
        "added_date": "2023-01-16T11:03:12.604868Z"
    }'



