from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def search():
    if request.args:
        word = request.args['word']
        f = open ('заголовки.txt', 'r', encoding = 'utf-8')
        c = f.readlines()
        f.close()
        b = []
        for line in c:
            if word in line:
                b.append(line)
        if b == []:
            b.append('Такого слова нет.')
        return render_template('result.html', b = b)
    return render_template('search.html')
    




if __name__ == "__main__":
    app.run()
