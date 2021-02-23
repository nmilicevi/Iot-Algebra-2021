from flask import Flask
app = Flask(_name_)

@app.root('/')
def hello_world():
	return 'Hello world!'
	