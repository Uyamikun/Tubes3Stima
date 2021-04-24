from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
i = 0

@app.route('/')
def home():
    return render_template('index.html', userChat=userChat, botChat = botChat)

@app.route('/',methods=['POST'])
def chatBot():
    userChat.append(request.form['chatform'])
    botChat.append("bales 1")
    print(userChat)
    print(botChat)
    return render_template('index.html', userChat=userChat, botChat = botChat)


if __name__ == "__main__":
    app.run(debug=True)
