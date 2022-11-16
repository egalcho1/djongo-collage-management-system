"""
Django settings for apparent project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-he2l9m16qa3@(^-*y@0jk!^ih2)#(l(lr^q#d0o%6hz5f(g9!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'main',
     'lectur',
     'human',
     'reg',
     'service',
     'library',
    'crispy_forms',
    'registeral.apps.RegisteralConfig',
    
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

ROOT_URLCONF = 'apparent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'main/template','registeral/templete','lectur/templete','human/template','reg/template','service/template','library/template'],
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

WSGI_APPLICATION = 'apparent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'egalcho', 
        'USER': 'root', 
        'PASSWORD': '',
        'HOST': '127.0.0.1', 
        'PORT': '3306',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'egalcho1@gmail.com'
EMAIL_HOST_PASSWORD = 'jbaunkdrhedsrknx'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
CRISPY_TEMPLATE_PACK='bootstrap4'
STATICFILES_DIRS = [
    BASE_DIR / "main/static",
   
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL='/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#password hasher
PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
  'django.contrib.auth.hashers.Argon2PasswordHasher',
  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  'django.contrib.auth.hashers.BCryptPasswordHasher',
  'django.contrib.auth.hashers.SHA1PasswordHasher',
  'django.contrib.auth.hashers.MD5PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
  'django.contrib.auth.hashers.CryptPasswordHasher',
]

#jazzman



JAZZMIN_SETTINGS = {
   
    "site_title": "addmin pannel",

   
    "site_header": "protected area",

   
    "site_brand": "online clearance",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "",

   
    "login_logo": None,

   
    "login_logo_dark": None,

   
    "site_logo_classes": "img-circle",
    "site_logo_width":"100",

    "site_icon": None,

    
    "welcome_sign": "welcome egalcho apparent project",

   
    "copyright": "egalcho",

    
    "search_model": "auth.User",

   
    "user_avatar": None,

   
    "topmenu_links": [

       
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

       
        {"model": "auth.User"},

      
        {"app": "books"},
    ],

   
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    
    "show_sidebar": True,

    
    "navigation_expanded": True,

    
    "hide_apps": [],

   
    "hide_models": [],

   
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

   
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

   
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
   
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

   
    "related_modal_active": False,

   
    "custom_css": None,
    "custom_js": None,
    
    "show_ui_builder": False,

   
    "changeform_format": "horizontal_tabs",
   
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
   
    #"language_chooser": True,
}
JAZZMIN_UI_TWEAKS = {
   
    "theme": "flatly",
    "dark_mode_theme": "darkly",
}

