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
def balesanBot(s):
    if(re.search("masuk", s) != None):
        return "Jadwal telah dimasukkan"
    else:
        return cekMatakuliah(s,arrayDataMatkul)

def cekTanggal(s):
    regextanggal = "(([0-2][0-9]|30|31)/([0][0-9]|10|11|12)/(20[0-9][0-9]|\\b[0-9][0-9]\\b))"
    regextanggalHuruf = "(([0-2][0-9]|30|31)) (([jJ]an|[fF]ebr)uari|[mM]aret|[aA]pril|[mM]ei|[jJ]uni|[jJ]uli|[aA]gustus|([sS]ept|[oO]ktob|[dD]es|[nN]ovemb)ember) (20[0-9][0-9]|\\b[0-9][0-9]\\b)"

    x = re.findall(regextanggal, s)
#    print(x)
    if(len(x) == 1):
        print(x[0][0])
        return x[0][0]
    else:
        x = re.findall(regextanggalHuruf, s)
#        print(x)
        if(len(x)==1):
            return x[0][0]
        else:
            return "gak"

# def cekContoh(s):
#     regex1 = "([0-2][0-9]|30|31)"
#     regex2 = "(([jJ]an|[fF]ebr)uari|[mM]aret|[aA]pril|[mM]ei|[jJ]uni|[jJ]uli|[aA]gustus|([sS]ept|[oO]ktob|[dD]es|[nN]ovemb)ember)"
#     regex3 = "([0-9]{2}|[0-9]{4})"
#     x = re.findall(regex1, s)
#     y = re.findall(regex2, s)
#     z = re.findall(regex3, s)
#     print(x,y,z)
#     if(len(x)==1):
#         return x[0]
#     elif(len(y)==1):
#         return y[0][0]
#     elif(len(z)==1):
#         return z[0]
#     else:
#         return "gak"

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
