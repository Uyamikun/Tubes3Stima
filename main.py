from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == "POST":
        #chattext = request.form['chattext']
        return redirect(url_for('static', filename='style.css'))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
