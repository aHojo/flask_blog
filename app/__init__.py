from flask import Flask
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

from . import routes  # noqa - This stops autopep8 from pushing it to the top of the file.
# . means inside this app package.
