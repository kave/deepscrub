from .base import *
import dj_database_url

if os.environ.get('DEBUG') == 'False':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

STATICFILES_STORAGE = 'core.storage.S3PipelineManifestStorage'
STATIC_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_YUGLIFY_BINARY = '/app/.heroku/python/bin/yuglify'
