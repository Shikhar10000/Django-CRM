import os

import dj_database_url
# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '19uaor)%xw51vl1l(1%xf*nam-*a==e221a#^)rnk&n!u6o#-z'


# Email Server Settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('SG_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('SG_PWD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Database Settings
DATABASES = {
    'default': dj_database_url.config(default='postgres://rtijkbfylevjrc:1249e0a38db98e871463b5134f7075f0c41a21a88a999712d1c26e12ecd98254@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/ddhd1h9qjmni38')    
}

# Server Customizations
ADMIN_EMAIL = "you@your_email.com"
URL_FOR_LINKS = "https://crm.example.com"


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
