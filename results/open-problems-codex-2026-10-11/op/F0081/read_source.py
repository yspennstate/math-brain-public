import pathlib,pymupdf
p=pathlib.Path('source.txt');p.write_text(p.read_text(encoding='utf8').replace('\x00',''),encoding='utf8')
d=pymupdf.open('source.pdf')
for i in [0,1,2,3,32,33,34]: print('\nPAGE',i+1,'\n',d[i].get_text())
