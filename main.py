from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)

userChat = ["pertama"]
botChat = ["balesan pertama"]
chat = [["pertama", 1], ["balesan pertama", 0]]
arrayTugas = []
arrayKataPenting = []
arrayDataMatkul = []
arrayScrapTopik = []
bulan = []
i = [0]

# baca konten penting
f = open("dataMataKuliah.txt",'r')
for item in f:
    arrayTemp = item.rstrip("\n").rsplit(',')
    for item2 in arrayTemp:
        arrayDataMatkul.append(item2)
f.close()

f = open("scrapForTopik.txt", 'r')
for item in f:
    arrayTemp = item.rstrip("\n").rsplit(',')
    for item2 in arrayTemp:
        arrayScrapTopik.append(item2)
f.close()
print(arrayScrapTopik)

f = open("katapenting.txt", 'r')
print(arrayDataMatkul)
for item in f:
    arrayTemp = item.rstrip("\n").rsplit(',')
    for item2 in arrayTemp:
        arrayKataPenting.append(item2)
f.close()

bulan = ["JANUARI", "FEBRUARI", "MARET", "APRIL", "MEI", "JUNI"]

# fungsi untuk bot, yang paling utama adalah fungsi balesan bot, sisanya fungsi pendukung
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
        return inputTask(s)


def inputTask(s):
    tanggal = cekTanggal(s)
    matkul = cekFromArray(s, arrayDataMatkul)
    jenis = cekFromArray(s, arrayKataPenting)
    print(jenis)
    print(tanggal, matkul, jenis)
    if(tanggal == "gak" or matkul == "ga ketemu" or jenis == "ga ketemu"):
        return "perintah tidak dikenali"
    indeksTanggal = re.search(tanggal, s).span()[0]
    indeksMatkul = re.search(matkul, s).span()[0]
    indeksJenis = re.search(jenis, s).span()[0]
    indeks = min(indeksJenis, indeksMatkul, indeksTanggal)
    buatTopik = s[indeks::]
    print(buatTopik)
    print(jenis)
    topik = buatTopik.replace(jenis,'', 1).replace(matkul, '', 1).replace(tanggal, '', 1)
    for i in arrayScrapTopik:
        topik = topik.replace(i.lower(), '')
    arrayTugas.append("{} - {} - {} - {}".format(convertTanggal(tanggal), matkul, jenis, topik))
    return "Task berhasil Dicatat:\n" + "{}. ".format(len(arrayTugas)) + arrayTugas[-1]

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

def convertTanggal(s):
    komponen = s.split(" ")
    print(komponen)
    if(len(komponen) == 1):
        return s
    else:
        return komponen[0] +"/" + "{0:02d}".format(bulan.index(komponen[1].upper()) + 1) + "/" + komponen[2][-2::] 


def cekFromArray(s, array):
    for item in array:
        indeks = booyer_moore(s, item)
        if(indeks != -1):
            return s[indeks:indeks+len(item)]
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
