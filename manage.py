from flask import Flask

app = Flask(__name__)

@app.route('/')
def Welcome_Users():
	return 'Welcome Users'

if __name__ == '__main__':
	app.run()
