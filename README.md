PLMmini (Product List Management MINI)
=====================

Overview
--------

PLMmini is a simple RESTful API service application for managing a product list.

Requirements:
-------------

	Python 3.10.8 (3.10.x working with Docker)
	Django 4.2
    Djangorestframework==3.14.0
    djangorestframework-api-key

Installation:
-------------


	Create new folder "PLMmini" and open it:
	git clone https://github.com/marcin86junior/PLMmini .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd product_manager\
	python manage.py migrate
	add SECRET_KEY = 'xxx' in settings.py
	python .\manage.py runserver
	http://127.0.0.1:8000/


Instructions:
-------
    1. Create super user: python .\manage.py createsuperuser
    2. Login on: http://127.0.0.1:8000/api/
    3. Please crete products on: http://127.0.0.1:8000/api/products/
        {
            "id": 1,
            "name": "Laptop",
            "description": "Laptop Samsung",
            "price": "120.00",
            "quantity": 6,
            "category": "KOMPUTERY",
            "created_at": "2024-06-03T20:23:54.896167Z"
        },
        {
            "id": 2,
            "name": "Tablet",
            "description": "Tablet Samsung",
            "price": "222.00",
            "quantity": 4,
            "category": "TABLETY",
            "created_at": "2024-06-03T20:33:38.931745Z"
        },
        {
            "id": 3,
            "name": "Tablet",
            "description": "Tablet Asus",
            "price": "111.00",
            "quantity": 2,
            "category": "TABLET",
            "created_at": "2024-06-03T21:19:59.630199Z"
        }
    4. Please edit product 2 on: http://127.0.0.1:8000/api/products/2/
    5. Please delete product 3 on: http://127.0.0.1:8000/api/products/3/
    6. Try search filter on: http://127.0.0.1:8000/api/products/


Todo list:
-------


    Implement API key authentication.
