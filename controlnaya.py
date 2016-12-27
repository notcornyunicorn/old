#Мизерова Катя, БКЛ-153
import os
import re
import json
from flask import Flask
from flask import render_template, request
app = Flask(__name__)
##
##n = os.listdir(path="C:\\Users\\student\\Desktop\\Контрольная\\thai_pages\\")
##for name in n:
##    name = "C:\\Users\\student\\Desktop\\Контрольная\\thai_pages\\"+name
##    f = open (name, 'r', encoding = 'utf-8')
##    s = f.readlines()
##    f.close()
##    a = s[len(s)-1]
##    b = a.split('<tr>')
##    for line in b:
##        file = open ('test.txt', 'a', encoding = 'utf-8')
##        if line.startswith('<td class=th>'):
##            file.write(line+'\n')
##            file.close()
##
##
##
def find_thai(line):
    reg = re.compile('<a href=\'\/id\/.*?\'>.*?</a>')
    word = reg.search(line)
    if word != None:
        thai = word.group(0)
        thai = re.sub('</?a( href=\'\/id\/.*?\')?>', "", thai)
        thai = re.sub('<img src=..img/camera.gif. />', "", thai)

        return thai
def find_translation(line):
    a = line.split('<td>')
    s = a[len(a)-1]
    s = re.sub('</td></tr>', "", s)
    return s
##    
##
##doc = open ('test.txt', 'r', encoding = 'utf-8')
##c = doc.readlines()
##doc.close()
##
##d = {}
##d1 = {}
##
##for line in c:
##    d[find_thai(line)] = find_translation(line).strip('\n')
##    d1[find_translation(line).strip('\n')] = find_thai(line)
##json_file = open ('thaidict.json', 'a')
##json_file.write (json.dumps(d)) #преобразовываем питоновский словарь (а еще можно массив) в джейсоновскую строку
##json_file.close()
##
##json_file1 = open ('engdict.json', 'a')
##json_file1.write (json.dumps(d1))
##json_file1.close()
##
@app.route('/search')
def search():
    if request.args:
        word = request.args['word']
        f = open ('test.txt', 'r', encoding = 'utf-8')
        c = f.readlines()
        f.close()
        b = []
        for line in c:
            if word in find_translation(line):
                b.append(word + ": "+ find_thai(line))
        if b == []:
            b.append('Извините, по вашему запросу ничего не найдено. Попробуйте ещё!')
        return render_template('result.html', b=b)
    return render_template('search.html')




if __name__ == "__main__":
    app.run()

    
