# Hans likes colors and to open webs

This is Hans, a speech recognizer. He can display 8 colors (the main colors) and open any website you desire. 

---

## Installation

Enter your desired directory in the terminal and do:

```bash
git clone https://github.com/Pallur/talgreinir.git
```

Or you can just save the zip file.

He was made using **Python3.7 64bit**. I have crafted a requirements.txt file, but I'm not sure if it's all of them. As I installed *many many* useless packages while working on it. :p

Usage:
```bash
pip install -r requirements.txt
```

If any "Can't find module x" come up when running, please first do
```bash
pip install x
```
or
```bash
python -m pip install x
```

To run Hans with flask you have to export the FLASK_APP environment variable:

**Linux** *(I think)*
* $ export FLASK_APP=main.py
* $ flask run
    "Running on http://127.0.0.1:5000/"

**Windows cmd**
* C:\path\to\app>set FLASK_APP=main.py
* python -m flask run
    "Running on http://127.0.0.1:5000/"

To get the CSS to work, you have to hard reset the browser. This is explained on the site it self *(hardcoded in the home.html)*

---

Now you might be asking "but why is 'it' named Hans?". 

