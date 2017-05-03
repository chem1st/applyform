from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['193.232.56.50', 'osmuss.muctr.ru']

DB_SERV = get_env_variable("DB_SERV")
DB_USER = get_env_variable("DB_USER")
DB_PASS = get_env_variable("DB_PASS")

DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "osmussdb",
    "USER": DB_USER,
    "PASSWORD": DB_PASS,
    "HOST": DB_SERV,
    "PORT": "3306",
    }
}

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles", "static")

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles", "media")