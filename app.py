# ---- Flask Hello World ---- #

#import the Flask class from the flask module
from flask import Flask #notice the caps

#create the application object
app = Flask(__name__)

#adding error handling
app.config["DEBUG"] = True 

# use decorators to create routes
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, World!?!?!?!"

#adding a new dynamic route
#adding a search query.
#whatever is input in the url it will output the same in the body
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#dynamic route that will return different status codes, i.e. 200 or 404
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

#messing around with different inputs types as routes

#interger
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

#float
@app.route("/float/<float:value>")
def float_type(value):
	print + 1
	return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"


# starts the development server using the run() method
if __name__ == "__main__":
	app.run()