from flask import Flask, render_template
from flask import request
from poll import Poll
import mlab

mlab.connect()

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        form = request.form
        key_word = form['search_engine']
        words = Poll.objects(input_trans = key_word).first()
        symnonyms = words['symnonyms_trans']
        return render_template('render_word.html', symnonyms = symnonyms)



@app.route("/eat")
def word():
    return render_template("word.html")

if __name__ == "__main__":
    app.run(debug = True)