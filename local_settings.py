DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'semesterly',
        'USER': 'rdietri3',
        'PASSWORD': 'Ryend15!!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
