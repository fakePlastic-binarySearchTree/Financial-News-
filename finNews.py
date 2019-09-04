####

import webbrowser as wb

def start():
    urls = ['https://www.bloomberg.com', 'http://www.ce.cn','http://www.morningwhistle.com','http://36kr.com','https://www.nytimes.com','https://www.ft.com']
    i = 0
    while i < len(urls):
        wb.open_new(urls[i])
        i = i + 1
    return 0

start()
