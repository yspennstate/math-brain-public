import requests,pathlib,concurrent.futures,xml.etree.ElementTree as E,json

def fetch(x):
 n,url=x
 try:
  r=requests.get(url,timeout=50);r.raise_for_status();pathlib.Path(n+'.pdf').write_bytes(r.content)
  import pymupdf
  d=pymupdf.open(n+'.pdf');text='\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d));pathlib.Path(n+'.txt').write_text(text,encoding='utf-8');print(n,'pages',len(d));print(text[:14500])
 except Exception as e:print(n,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(fetch,[('zhang','https://arxiv.org/pdf/math/0301160'),('ziff','https://arxiv.org/pdf/1602.00644')]))
ns={'a':'http://www.w3.org/2005/Atom'};t=E.parse('arxiv.response')
for e in t.findall('a:entry',ns):
 if any(y in e.findtext('a:id',namespaces=ns) for y in ['0301160','1602.00644','1107.0158']):print(E.tostring(e,encoding='unicode'))
