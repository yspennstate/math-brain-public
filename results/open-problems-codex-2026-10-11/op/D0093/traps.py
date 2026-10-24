import pymupdf
p=pymupdf.open('rolla.pdf')
for i in range(17,22): print('PAGE',i+1,p[i].get_text())
