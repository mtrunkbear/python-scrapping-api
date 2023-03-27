from flask import Flask

application = Flask(__name__)

from app.controllers import *

if __name__ == '__main__':
    application.run(port=8000)