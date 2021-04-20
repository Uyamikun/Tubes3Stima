from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST','GET'])
def hasil():
    # #click submit, get the data
    if request.method == "POST":
        chattext = request.form['chattext']
        return f"<h1>{chattext}</h1>" 
    else:
        return render_template('chat.html')

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
