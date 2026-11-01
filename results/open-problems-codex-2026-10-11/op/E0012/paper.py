import urllib.request,pathlib,json,xml.etree.ElementTree as ET
urls={'allelopathy':'https://arxiv.org/pdf/2305.17016','crossref_exact':'https://api.crossref.org/works?query.title=Durrett-Levin%20spatial%20model%20of%20allelopathy&rows=5'}
for k,u in urls.items():
 try:
  data=urllib.request.urlopen(u,timeout=40).read();pathlib.Path(k+('.pdf' if k=='allelopathy' else '.json')).write_bytes(data)
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n2026-10-12 fetched '+u+' OK\n')
 except Exception as e:print(e)
import pymupdf
doc=pymupdf.open('allelopathy.pdf')
pathlib.Path('allelopathy.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf8')
for i,p in enumerate(doc):
 if i<6:print('PAGE',i+1,p.get_text())
a=json.load(open('semantic_retry.json',encoding='utf8'))
for c in a.get('data',[]):print('CITING',c)
