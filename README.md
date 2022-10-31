# Event App

## Steps to run the app

1. Create virtual environment by running , here's a [tutorial](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
2. activate virtualenv
3. install requirements in your virtual environment running:
`pip install -r requirements.txt`
4. run `python manage.py migrate`
5. run `python manage.py createsuperuser` to create admin user
6. run `python manage.py runserver`
7. login to localhost:8000/admin using superuser creds
8. Now you can create rooms, events and use other methods