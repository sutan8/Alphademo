from flask import Flask
from config import Config

print('init running...')
app = Flask(__name__)
print('app=Flask(name) ran')
app.config.from_object(Config)
from app import routes, motorctl

