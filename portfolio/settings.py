import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# 🔴 FIX 1: Gumamit ng Environment Variable para sa SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY')

# WARNING: Don't run with debug turned on in production!
# Tiyakin na ito ay 'False' sa production
DEBUG = False 

# 🔴 FIX 2: ALLOWED_HOSTS para sa Render URL
ALLOWED_HOSTS = [
    'garciacorrea-portfolio-2.onrender.com', # Ang Render URL
    '.onrender.com', # Added wildcard for safety
    '127.0.0.1', 
    'localhost',
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', # I assume ito ang app name mo
]

# 🔴 FIX 3: MIDDLEWARE order (Whitenoise)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ⬅️ Dito dapat nakalagay
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database configuration (default SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# ... (Leave default password validation settings)
# ...

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 🔴 FIX 4: Static and Media File Settings
STATIC_URL = 'static/'
# Lokasyon ng iyong static files sa lokal na repository
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# Output directory kapag nag-collectstatic sa Render
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Whitenoise storage


# Para sa images (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'