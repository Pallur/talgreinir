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

---

Þegar ég byrjaði á verkefninu var ég að fikta mikið með það sem hægt er að finna á tal.ru.is. Fann út að sú síða er byggð á [kalda](https://github.com/kaldi-asr/kaldi). Eftir að hafa verið að reyna að setja það upp á windows í heil langan tíma þá fór ég í það að setja upp Virtual vél og keyra Ubuntu á henni því ég bjóst við að það væri lítið mál að nota Linux með þessu.. **__það gékk ekki_**. 

Eftir þetta ævintýri fór ég að reyna smíða minn eigin 'Speech Recognizer'. Ég byrjaði á að nota Spyder3 IDE umhverfið við þróunina og allt gekk einsog í sögu (svona næstum). Svo fór ég útí það að reyna að fá kóðann til að keyra á netinu. Ég ákvað að nota flask í þetta. 

Til að gera langa sögu stutta, þá virkaði ekkert hjá mér **virkilega** lengi útaf Python-ið sem ég var að nota í cmd var 32bit en ekki 64bit einsog í Spyder3. Eftir að síðan komst í loftið vissi ég ekki alveg hvað ég vildi láta *Hans* gera nákvæmlega. Svo ég fór bara útí eitthvað einfalt en samt ágætlega skemmtilegt. 

Vona hann standi sig vel.

