from flask import Flask

#create flask app
app = Flask(__name__)


#create route
@app.route('/')
def hello_world():
	return 'Hello world and Australia'
