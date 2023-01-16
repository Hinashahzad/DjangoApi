# DjangoApi

## Introduction
Creating Backend using Python Framework Django

## Installation dependeancy

`pip install python`
`pip install django`
`pip install djangorestframework`
`django-admin startproject apiProject`

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

## Create APP for creating the django api
`python manage.py startapp api`

## Create the MODEL by using the following command in terminal
`python manage.py makemigrations` 

## To reflects the changings into the database (Send data from MODEL to DATABASE ) use the following command in terminal
`python manage.py migrate`

## Install Postman 



