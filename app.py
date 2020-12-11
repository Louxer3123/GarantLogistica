import os
import datetime

from flask import Flask
from flask_login import LoginManager


db = 'sqlite:///garant_logistica.db'
DEBUG = True
SECRET_KEY = os.urandom(42)

app = Flask(__name__)
app.config.from_object(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=10)

app.config.update(dict(db=os.path.join(app.root_path, 'garant_logistica.db')))
login_manager = LoginManager(app)

