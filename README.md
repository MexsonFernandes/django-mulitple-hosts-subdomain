# Django Multiple Host on Subdomain (Boilerplate)

Host Django apps on multiple subdomains. This repository is just a boilerplate to get started with Django hosts.

<a href='https://ko-fi.com/Y8Y31LBT4' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## How to start?

* Clone repo `git clone https://github.com/MexsonFernandes/django-mulitple-hosts-subdomain`.
* Go to directory `cd django-mulitple-hosts-subdomain`.
* Install environment using Pipenv `pipenv shell`. Use `pip3 install pipenv` if not installed.
* Install all requirements using `pipenv install` or `pip3 install -r requirements.txt`.
* Run app using `python manage.py runserver`.

## How to check?

* open default app at http://www.localhost:8000
* open admin at http://admin.localhost:8000
* open installed app at http://app2.localhost:8000

## How to add hosts?

* Add new app using `django-admin startapp newapp`.
* Register app in settings.py under *MY_APP*.
* Create urls.py file with initial route.
* Add it as host in 'django_subdomains_project/hosts.py'.

## How to change default route?

* Go to 'django_subdomains_project/settings.py' and change app name in DEFAULT_HOST variable.

Thanks for checking out my repo. Explore my profile at [Linkedin](https://www.linkedin.com/mexsonfernandes).
