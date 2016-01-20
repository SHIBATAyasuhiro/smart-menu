from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('smartMenu.config')
db = SQLAlchemy(app)

import smartMenu.views