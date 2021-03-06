"""
Django settings for fake_twitter_site project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f0*yr3*#4x)+2!bt%-o&dmb*n4cfjvcl+v-48srmn#!$x-43o!'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('heroku'):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','fake----twitter.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fake_twitter_profile',
    'tweet',
    'register',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fake_twitter_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,''), os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fake_twitter_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER':'root',
        'PORT' : '5432'
    }
}
if DEBUG:
    DATABASES['default']['ENGINE']='django.db.backends.postgresql'
    DATABASES['default']['HOST']='db'
    DATABASES['default']['NAME']='db'
    DATABASES['default']['PASSWORD']='qwerty'
else:
    # ここは書き換える必要があるかもしれない
    DATABASES['default']['ENGINE']='django.db.backends.postgresql'
    DATABASES['default']['USER']='hdaksjfrthuljh'
    DATABASES['default']['PASSWORD']='2062131a1842ed662c64e749f17a76cb5641c7c65715072aa43f77d802e451ac'
    DATABASES['default']['HOST']='ec2-54-83-36-37.compute-1.amazonaws.com'
    DATABASES['default']['NAME']='devdqkf3ggqj0i'
    

    

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#LOGIN_URL = 'login' # ログインしていないときのリダイレクト先
#LOGIN_REDIRECT_URL ='index' # ログイン後のリダイレクト先
#LOGOUT_REDIRECT_URL = 'top' # ログアウト後のリダイレクト先

APPEND_SLASH=False 



