from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)

chat = []
arrayTugas = []
arrayKataPenting = []
arrayDataMatkul = []
arrayScrapTopik = []
arrayPrintTask = []
bulan = ["JANUARI", "FEBRUARI", "MARET", "APRIL", "MEI", "JUNI"]
i = [0]

#readfile masukkin ke array
def readFile(filename,array):
    f = open("database/"+ filename , 'r')
    for item in f:
        arrayTemp = item.rstrip("\n").rsplit(',')
        for item2 in arrayTemp:
            array.append(item2)
    f.close()
# baca konten penting
readFile("dataMataKuliah.txt",arrayDataMatkul)
readFile("katapenting.txt",arrayKataPenting)
readFile("kataPentingPrintTask.txt",arrayPrintTask)
readFile("scrapForTopik.txt",arrayScrapTopik)

def balesanBot(s):        
    #inputTask
    temp = inputTask(s)
    if(temp != ""):
            return temp
    if(checkTask(s) != ""):
        return checkTask(s)
    temp = checkPrintTask(s,arrayTugas,arrayPrintTask)
    if(temp != ""):
        return temp
    temp = undurDeadline(s, arrayTugas)
    if(temp != ""):
        return temp
    temp = selesaiTask(s)
    if(temp != ""):
        return temp
    temp = checkPrintTaskJuga(s, arrayTugas, arrayPrintTask, arrayKataPenting)
    if(temp != ""):
        return temp
    return "Perintah tidak dikenal"
            

# fungsi untuk bot, yang paling utama adalah fungsi balesan bot, sisanya fungsi pendukung
def booyer_moore(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    #print(pattern, " | ", text)
    last = buildLast(pattern)
    n = len(text); m = len(pattern)
    i = m-1
    if(i > n-1):
        return -1
    j = m-1
    while(i <= n-1):
        if(pattern[j] == text[i]):
            if(j==0):
                return i
            else:
                i -= 1
                j -= 1
        else:
            location = last[ord(text[i])]
            #print(i, j, location)
            i = i+m-min(j, 1+location)
            j = m-1
    return -1

def buildLast(pattern):
    #print(pattern, len(pattern))
    last = [-1 for i in range(128)]
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last

def inputTask(s):
    tanggal = cekTanggal(s)
    matkul = cekFromArray(s, arrayDataMatkul)
    jenis = cekFromArray(s, arrayKataPenting)
    #print(jenis)
    #print(tanggal, matkul, jenis)
    if(tanggal == "gak" or matkul == "ga ketemu" or jenis == "ga ketemu"):
        return ""
    indeksTanggal = re.search(tanggal, s).span()[0]
    indeksMatkul = re.search(matkul, s).span()[0]
    indeksJenis = re.search(jenis, s).span()[0]
    indeks = min(indeksJenis, indeksMatkul, indeksTanggal)
    buatTopik = s[indeks::]
    #print(buatTopik)
    #print(jenis)
    topik = buatTopik.replace(jenis,'', 1).replace(matkul, '', 1).replace(tanggal, '', 1)
    topik = " ".join(topik.split())
    for i in arrayScrapTopik:
        topik = topik.replace(i.lower(), '')
    arrayTugas.append("{} - {} - {} - {}".format(convertTanggal(tanggal), matkul, jenis, topik))
    return "Task berhasil Dicatat:\n" + "{}. ".format(len(arrayTugas)) + arrayTugas[-1]

def checkTask(s):
    # harus ada kata deadline, terus ada juga kata tugas/pr/makalah
    deadline = booyer_moore(s, "deadline")
    tugas = booyer_moore(s, " tugas")
    pr = booyer_moore(s, " pr")
    makalah = booyer_moore(s, " makalah")
    # tanggal = cekTanggal(s)
    matkul = cekFromArray(s, arrayDataMatkul)
    #print(s, arrayDataMatkul)
    #print(deadline, tugas+pr+makalah, matkul)
    if(matkul == "ga ketemu"):
        return ""
    for i in arrayTugas:
        perkata = i.split(" - ")
        #print(perkata)
        if(deadline != -1 and tugas+pr+makalah != -3 and perkata[1] == matkul):
            if(tugas != -1 and perkata[2][0:2].lower() == "tu"):
                return perkata[0]
            elif(pr != -1 and perkata[2].lower() == "pr"):
                return perkata[0]
            elif(makalah != -1 and perkata[2].lower() == "makalah"):
                return perkata[0]
    return ""
        
def cekTanggal(s):
    regextanggal = "(([0-2][0-9]|30|31)/([0][0-9]|10|11|12)/(20[0-9][0-9]|\\b[0-9][0-9]\\b))"
    regextanggalHuruf = "(([0-2][0-9]|30|31) (([jJ]an|[fF]ebr)uari|[mM]aret|[aA]pril|[mM]ei|[jJ]uni|[jJ]uli|[aA]gustus|([sS]ept|[oO]ktob|[dD]es|[nN]ovemb)ember) (20[0-9][0-9]|\\b[0-9][0-9]\\b))"

    x = re.findall(regextanggal, s)
    #print(x)
    if(len(x) == 1):
        #print(x[0][0])
        return x[0][0]
    else:
        x = re.findall(regextanggalHuruf, s)
        #print(x)
        if(len(x)==1):
            return x[0][0]
        else:
            return "gak"

def convertTanggal(s):
    komponen = s.split(" ")
    #print(komponen)
    if(len(komponen) == 1):
        return s
    else:
        return komponen[0] +"/" + "{0:02d}".format(bulan.index(komponen[1].upper()) + 1) + "/" + komponen[2][-2::] 

def cekFromArray(s, array):
    for item in array:
        indeks = booyer_moore(s, item)
        #print(indeks)
        if(indeks != -1):
            return s[indeks:indeks+len(item)]
    return "ga ketemu"


def selesaiTask(s):
    selesai = booyer_moore(s, "selesai")
    task = booyer_moore(s, "task")
    id = ""
    if(selesai != -1 and task != -1):
        task += 5
        while(task < len(s) and s[task] != " "):
            id = id + s[task]
            task += 1
        id = int(id)
        if(id <= len(arrayTugas) and id > 0):
            arrayTugas.pop(id-1)
            return "task dengan id {} berhasil dihapuskan".format(id)
        return "tidak terdapat task dengan id tersebut"
    return ""

#Nomor 2 Print Task
def checkPrintTask(s,arrayTugas,arrayPrintTask):
    deadline = booyer_moore(s, "deadline")
    nodate = booyer_moore(s," sejauh")
    if(deadline != -1 and nodate != -1):
        return printAllTask(arrayTugas)
    elif(deadline != -1 and cekFromArray(s,arrayPrintTask) != "ga ketemu"):
        tanggal1 = cekTanggal(s)
        s.replace(tanggal1,"")
        tanggal2 = cekTanggal(s)
        #if(tanggal1 != "gak" or tanggal2 != "gak"):
    return ""

def checkPrintTaskJuga(s,arrayTugas,arrayPrintTask, arrayKataPenting):
    deadline = booyer_moore(s, "deadline")

    #bagian barunya(cek pake task)
    penting = cekFromArray(s, arrayKataPenting).lower()
    if(deadline != -1 and penting != "ga ketemu"):
        hasil = "Deadline yang anda miliki: "
        index = 1
        for item in arrayTugas:
            pecahan = item.split( ' - ')
            if(pecahan[2].lower() == penting.lower()):
                hasil += "\n" + str(index) + ". " + item
                index += 1
        if(hasil == "Deadline yang anda miliki: "):
            return "tidak ada deadline yang memenuhi"
        return hasil
    return ""

def printAllTask(arrayTugas):
    temp = "List tugas yang tersimpan :\n "
    count = 1
    for item in arrayTugas:
        temp += str(count) + ". "+item + "\n"
        count+= 1
    return temp

def undurDeadline(s, array):
    undur = booyer_moore(s, "undur")
    task = booyer_moore(s, "task")
    tanggal = cekTanggal(s)
    id = ""
    if(undur != -1 and task != -1 and tanggal != "gak"):
        tanggal = convertTanggal(tanggal)
        task += 5
        while(task < len(s) and s[task] != " "):
            print("element setelah task:", s[task]) 
            id = id + s[task]
            task += 1
        id = int(id)
        if(id <= len(arrayTugas) and id > 0):
            pecahan = array[id-1].split(" - ", 1)
            array[id-1] = tanggal + " - " + pecahan[1]
            return "task dengan id {} berhasil diundur menjadi {}".format(id, tanggal)
        return "tidak terdapat task dengan id tersebut"
    return ""

@app.route('/')
def home():
    chat.clear()
    return render_template('index.html', chat = chat)

@app.route('/',methods=['POST'])
def chatBot():
    pesan = request.form['chatform']
    chat.append([pesan, 1])
    chat.append([balesanBot(pesan), 0])
    print("====== this is chat list ======")
    print(chat)
    return render_template('index.html', chat = chat)


if __name__ == "__main__":
    app.run(debug=True)
