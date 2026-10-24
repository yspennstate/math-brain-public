import urllib.request,pathlib,json
u='https://alea.impa.br/articles/v21/21-14.pdf'
try:
 d=urllib.request.urlopen(u,timeout=40).read();pathlib.Path('journal_2024.pdf').write_bytes(d)
 with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n2026-10-12 journal version fetch '+u+' OK\n')
 import pymupdf
 p=pymupdf.open('journal_2024.pdf');pathlib.Path('journal_2024.txt').write_text('\n'.join(x.get_text() for x in p),encoding='utf8')
 for i in range(min(6,len(p))):print('JOURNAL PDF PAGE',i+1,p[i].get_text())
except Exception as e:print('JOURNAL ERROR',repr(e))
w=json.load(open('crossref_exact.json',encoding='utf8'))['message']['items'][0]
print('REFERENCE',w.get('title'),w.get('author'),w.get('volume'),w.get('page'),w.get('container-title'),w.get('DOI'))
