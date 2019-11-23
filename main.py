from flask import Flask, render_template, request, redirect, url_for
from mypackage.hans import voice_command, assistant
from mypackage.colorapi import color_api, name_hex

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/command', methods=['GET', 'POST'])
def your_command():
    if request.method == 'POST':
        vc = voice_command()
        # print("vc er: ", vc)
        color_hex = name_hex(color_api())
        for c, h in color_hex:
            # print("sup bitch", c)
            if vc == c.lower():
                print("hallo u whore")
                return render_template("home.html", cname = c, chex = h, command = vc)
        
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
