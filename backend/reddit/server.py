from flask import Flask
from reddit import rest

class Reddit(Flask):
    def __init__(self, import_name):
        super(Reddit, self).__init__(import_name, static_url_path='')

    def init(self):
        modules = [
            rest
        ]

        for module in modules:
            module.initialize(self)


def create_app():
    """Creates Flask app instance"""
    app = Reddit(__name__)
    return app