from flask import Flask, render_template, request, redirect, url_for
import bot
app = Flask(__name__)

chat = []
            


@app.route('/')
def home():
    # chat.clear()
    return render_template('index.html', chat = chat)

@app.route('/',methods=['POST'])
def chatBot():
    pesan = request.form['chatform']
    chat.append([pesan, 1])
    chat.append([bot.balesanBot(pesan), 0])
    if(len(chat) > 100):
        chat.pop(0)
        chat.pop(0)
    #print("====== this is chat list ======")
    #print(chat)
    return render_template('index.html', chat = chat)


if __name__ == "__main__":
    app.run(debug=True)
