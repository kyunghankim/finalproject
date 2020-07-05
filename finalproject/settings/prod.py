from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False # 추후에 False로 변경 예정

ALLOWED_HOSTS = [
    '54.180.2.36',
    '.compute.amazonaws.com',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')