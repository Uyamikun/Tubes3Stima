from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
chat = [["pertama", 1], ["balesan pertama", 0]]
i = [0]

def balesanBot(s):
    if(re.search("masuk", s) != None):
        return "Jadwal telah dimasukkan"

@app.route('/')
def home():
    return render_template('index.html', chat = chat)

@app.route('/',methods=['POST'])
def chatBot():
    pesan = request.form['chatform']
    chat.append([pesan, 1])
    chat.append([balesanBot(pesan), 0])
    print(chat)
    return render_template('index.html', chat = chat)


if __name__ == "__main__":
    app.run(debug=True)
