from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.py')

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')
