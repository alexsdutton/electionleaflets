from .base import *

LETTUCE_USE_TEST_DATABASE = True
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MEDIA_ROOT = MEDIA_ROOT = root('test_media', )

SPATIALITE_LIBRARY_PATH='/usr/local/lib/mod_spatialite.dylib'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': '/tmp/electionleaflets.db',
    },
    'test': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': '/tmp/electionleaflets.db',
    }
}