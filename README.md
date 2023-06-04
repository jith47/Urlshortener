# Urlshortener.     
A web app which shortens long urls by replacing a unique short url attached with domain name and unique shortcode.
It also provides service to store them in a Django admin accesible database, which enables manipulation of data.

Note:
    This app is deployable (**tested with Heroku AI) .You can deploy it on your site after providing site url as DEFAULT_REDIRECT_URL in settings.py
    
    
    
    
#use command "python manage.py runserver" to test this app in local server

Setup cmds:
    pip install django-hosts
    python manage.py migrate
    python manage.py collectstatic