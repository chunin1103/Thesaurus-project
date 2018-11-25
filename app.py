from flask import Flask, render_template
from flask import request
from poll import Poll
import mlab
from word import search_for

mlab.connect()

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        form        = request.form
        key_word    = form['search_engine']
        words       = Poll.objects(input_trans = key_word.lower()).first()
        suggestions = Poll.objects()
        if words is not None:
            symnonyms   = words['symnonyms_trans']
            return render_template('render_word.html', symnonyms = symnonyms, key_word=key_word)
        else: 
            return render_template('error.html', key_word=key_word, suggestions=suggestions)


@app.route("/eat")
def word():
    return render_template("word.html")

if __name__ == "__main__":
    app.run(debug = True)