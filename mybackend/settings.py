from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret')
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    os.getenv('RENDER_EXTERNAL_HOSTNAME', ''),
]

# Use our custom user with email-as-username
AUTH_USER_MODEL = 'accounts.CustomUser'

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}

AUTHENTICATION_BACKENDS = [
    'djoser.auth_backends.LoginFieldBackend',    # ← lets users log in with email
    'django.contrib.auth.backends.ModelBackend', # ← fallback (admin, etc.)
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'accounts',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'symphonious-licorice-91a25d.netlify.app',  # Add this
    os.getenv('RENDER_EXTERNAL_HOSTNAME', ''),
]


# For development only - be more restrictive in production
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'mybackend.urls'
WSGI_APPLICATION = 'mybackend.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],                 # ← or list any custom template dirs you use
        'APP_DIRS': True,           # ← so Django will look inside each app’s “templates/”
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

# DRF + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Djoser config: signup, password-reset, and JWT (email-based) all “just work”
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_ID_FIELD': 'id',
    'SEND_ACTIVATION_EMAIL': False,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'PASSWORD_RESET_CONFIRM_URL': 'reset-password.html?uid={uid}&token={token}',
    'DOMAIN': 'symphonious-licorice-91a25d.netlify.app',
    'SITE_NAME': 'AumOui Lifestyle Essentials',
    'PROTOCOL': 'https',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'FRONTEND_URL': 'https://symphonious-licorice-91a25d.netlify.app',  # Add this
}



# Brevo SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('BREVO_SMTP_HOST')
EMAIL_PORT = int(os.getenv('BREVO_SMTP_PORT', 587))
EMAIL_HOST_USER = os.getenv('BREVO_SMTP_USER')
EMAIL_HOST_PASSWORD = os.getenv('BREVO_SMTP_PASS')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
