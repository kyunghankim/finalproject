from .base import *
from decouple import config

#decouple의 config를 활용해 secret key 숨기기!!
SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []