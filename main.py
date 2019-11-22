from flask import Flask, render_template, request, redirect, url_for
# from mypackage.tester import *
from mypackage.hans import voice_command, assistant, hans_response
# from mypackage.hans import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", class_id = None)

@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    if request.method == 'GET':
        return render_template("home.html", comments=comments)
    comments.append(request.form["text_input"])
    return redirect(url_for('text'))

@app.route('/command', methods=['GET', 'POST'])
def your_command():
    if request.method == 'POST':
        vc = voice_command() 
        return render_template("home.html", box_id = vc, command = vc)
    if request.method == 'GET':
        vc = voice_command()
        return render_template("home.html", box_id = vc, command = vc)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
