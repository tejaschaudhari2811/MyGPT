from flask import Flask

app = Flask(__name__, template_folder="./../frontend/html", static_folder="./../frontend/static")