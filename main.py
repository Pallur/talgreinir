from flask import Flask, render_template, request, redirect, url_for
from mypackage.hans import voice_command, assistant
from mypackage.colorapi import color_api, name_hex
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

# ! if 'DYNO' in os.envirion:
# !    sslify = SSLify(app)

# * default page
@app.route('/')
def home():
    return render_template("home.html")

# * command page
@app.route('/command', methods=['GET', 'POST'])
def your_command():
    if request.method == 'POST':
        vc = voice_command()
        color_hex = name_hex(color_api())
        for c, h in color_hex:
            if vc == c.lower():
                # * if color exist, the color will be shown
                return render_template("home.html", cname = c, chex = h, command = vc)
    
    # * if no match, a message will be shown
    return render_template("home.html", no_color = "No color found", command = vc)
        
# * open page page
@app.route('/open', methods=['GET', 'POST'])
def open_web():
    if request.method == 'POST':
        website = assistant(voice_command())
        return render_template("home.html", open = website)

if __name__ == "__main__":
    app.run(debug=True)
