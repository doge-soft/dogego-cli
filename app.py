# -*- encoding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from handlers.create_api import CreateAPI
from handlers.create_mvc import CreateMVC

app = Flask(__name__)
manager = Manager(app)

manager.add_command("create-api", CreateAPI)
manager.add_command("create-mvc", CreateMVC)

manager.run()
