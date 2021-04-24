from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
chat = [["pertama", 1], ["balesan pertama", 0]]
arrayTugas = []
i = [0]

def balesanBot(s):
    if(re.search("masuk", s) != None):
        return "Jadwal telah dimasukkan"
    else:
        return cekTanggal(s)

def cekTanggal(s):
    regextanggal = ^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$
    x = re.findall(regextanggal, s)
    print(x)
    if(len(x) == 1):
        return x[0]
    else:
        return "gak"

def cekMatakuliah(s):
    #ambil input cek input di listMatakuliah
    regexmatkul = "IF2222"
    x = re.findall(regexmatkul,s)
    if(len(x) == 1):
        return x[0]
    else:
        return "tidak ada"
def createTask(tanggal,matakuliah,jenis,topik,arrayTugas):
    tempTask = [tanggal,matakuliah,jenis,topik]
    arrayTugas.append(tempTask)



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
