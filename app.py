from flask import Flask
from config import config


app = Flask(__name__)


app.config.from_object(config["development"])  



if __name__ == '__main__':
    app.run()
