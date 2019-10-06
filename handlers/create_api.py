from cookiecutter.main import cookiecutter
from flask_script import Command

class CreateAPI(Command):
    def run(self):
        cookiecutter("https://github.com/doge-soft/dogego")
