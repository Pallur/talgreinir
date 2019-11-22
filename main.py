from flask import Flask, render_template, request, redirect, url_for
from mypackage.hans import voice_command, assistant

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", class_id = None)

@app.route('/command', methods=['GET', 'POST'])
def your_command():
    if request.method == 'POST':
        vc = voice_command() 
        return render_template("home.html", box_id = vc, command = vc)
    if request.method == 'GET':
        vc = voice_command()
        return render_template("home.html", box_id = vc, command = vc)
    
@app.route('/open', methods=['GET', 'POST'])
def open_web():
    if request.method == 'POST':
        website = assistant(voice_command())
        return render_template("home.html", open = website)

if __name__ == "__main__":
    app.run(debug=True)
