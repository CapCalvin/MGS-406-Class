from flask import Flask

app = Flask(__name__)

@app.route('/greetings/newyear')

def newyear():
	return 'Happy New Year!'

if __name__ == '__main__':
	app.run()
