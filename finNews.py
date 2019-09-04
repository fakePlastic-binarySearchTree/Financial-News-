####

####
#pwd (get pathway)
#(base) CUILINs-MacBook:Desktop cuicui$ cd ~/Desktop/Folder Name
#(base) CUILINs-MacBook:Desktop cuicui$ python ./test.py
#open filename.docx(or type)         (open file)
#python ./filename.py                (run file)

#python (open python, can code here directly)
#f = open('filename.py')
#exit()       (exit python)

import webbrowser as wb

def start():
    urls = ['https://www.bloomberg.com', 'http://www.ce.cn','http://www.morningwhistle.com','http://36kr.com','https://www.nytimes.com','https://www.ft.com']
    i = 0
    while i < len(urls):
        wb.open_new(urls[i])
        i = i + 1
    return 0

start()





        

