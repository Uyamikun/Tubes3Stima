from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
chat = [["pertama", 1], ["balesan pertama", 0]]
i = [0]

@app.route('/')
def home():
    return render_template('index.html', chat = chat)

@app.route('/',methods=['POST'])
def chatBot():
    i.append(i[-1]+1)
    chat.append([request.form['chatform'], 1])
    chat.append(["bales " + str(i[-1]), 0])
    print(chat)
    return render_template('index.html', chat = chat)


if __name__ == "__main__":
    app.run(debug=True)
