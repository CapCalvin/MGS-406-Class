from flask import Flask

app = Flask(__name__)

@app.route('/greetings/Christmas')

def christmas():
	return 'Merry Christmas!'


if __name__ == '__main__':
	app.run()


