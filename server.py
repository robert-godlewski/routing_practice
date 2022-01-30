from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world(): return 'Hello World!'

@app.route('/dojo')
def dojo(): return 'Dojo!'

@app.route('/say/<phrase>')
def say_phrase(phrase): return f"Hi {str(phrase)}!"

@app.route('/repeat/<times>/<phrase>')
def repeat(times, phrase):
    num_times = int(times)
    str_phrase = str(phrase)
    i = 0
    while i < num_times:
        print(str_phrase)
        i += 1
    return str_phrase

@app.route('/<blah>')
def error(blah):
    if blah != 'dojo' or 'say/' or 'repeat/': 
        return "Sorry! No response. Try again."


if __name__=="__main__": app.run(debug=True)