from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
chat = [["pertama", 1], ["balesan pertama", 0]]
arrayTugas = []
arrayKataPenting = []
arrayDataMatkul = []
i = [0]

#
f = open("dataMataKuliah.txt",'r')
for item in f:
    arrayTemp = item.rstrip("\n").rsplit(',')
    for item2 in arrayTemp:
        arrayDataMatkul.append(item2)
print(arrayDataMatkul)

def booyer_moore(text, pattern):
    last = buildLast(pattern)
    n = len(text); m = len(pattern)
    i = m-1
    if(i > n-1):
        return -1
    j = m-1
    while(i <= n-1):
        if(pattern[j].upper() == text[i].upper()):
            if(j==0):
                return i
            else:
                i -= 1
                j -= 1
        else:
            location = last[ord(text[i].upper())]
            i = i+m-min(j, 1+location)
    return -1


def buildLast(pattern):
    last = [-1 for i in range(128)]
    for i in range(len(pattern)):
        last[ord(pattern[i].upper())] = i
    return last


def balesanBot(s):
    if(re.search("masuk", s) != None):
        return "Jadwal telah dimasukkan"
    else:
        # return cekMatakuliah(s,arrayDataMatkul)
        return cekTanggal(s)

def cekTanggal(s):
    regextanggal = "(([0-2][0-9]|30|31)/([0][0-9]|10|11|12)/(20[0-9][0-9]|\\b[0-9][0-9]\\b))"
    regextanggalHuruf = "(([0-2][0-9]|30|31) (([jJ]an|[fF]ebr)uari|[mM]aret|[aA]pril|[mM]ei|[jJ]uni|[jJ]uli|[aA]gustus|([sS]ept|[oO]ktob|[dD]es|[nN]ovemb)ember) (20[0-9][0-9]|\\b[0-9][0-9]\\b))"

    x = re.findall(regextanggal, s)
    print(x)
    if(len(x) == 1):
        print(x[0][0])
        return x[0][0]
    else:
        x = re.findall(regextanggalHuruf, s)
        print(x)
        if(len(x)==1):
            return x[0][0]
        else:
            return "gak"


def cekMatakuliah(s,arrayDataMatkul):
    #ambil input cek input di listMatakuliah
    for item in arrayDataMatkul:
        if((re.match(s, item, re.IGNORECASE))):
            found = True
            return "ketemu"
        else:
            found = False
    return "ga ketemu"

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
