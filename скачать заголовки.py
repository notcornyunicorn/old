import urllib.request
import re
import html

def download_page(pageUrl): 
    try:
        page = urllib.request.Request(pageUrl)
        with urllib.request.urlopen(page) as response:
            html = response.read().decode('utf-8')
    except:
        print('Error at', pageUrl)
    return html

def clear_html (unclear_text):
    reg = re.compile('<li>.*?</li>', flags=re.U | re.DOTALL)
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL) 
    a = []
    text = reg.findall(unclear_text)
    for title in text:
        title = regTag.sub("", title)
        title = html.unescape(title)
        a.append(title)
    return a

def write_file(a):
    for title in a:
        f = open('заголовки.txt', 'a', encoding = 'utf-8')
        f.write(title + '\n')
        f.close()
    return print('Всё записалось. Ура!')

pageUrl = 'http://www.marpravda.ru/'

write_file(clear_html(download_page(pageUrl)))
