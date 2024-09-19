from flask import render_template

class Website:
    def __init__(self, app) -> None:
        self.app = app
        self.routes = {
            '/':{
                'function': self._index,
                'methods' : ["GET", "POST"]
            }
        }
    
    def _index(self):
        return render_template("index.html")