import urllib.request,concurrent.futures,json
from pathlib import Path
urls={x:'https://arxiv.org/pdf/'+x for x in ['1901.03617','2512.08151','2403.01658']}
urls.update({'openalex_retry':'https://api.openalex.org/works?search=Three%20puzzles%20mathematics%20computation%20games&per-page=5','semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1801.02602/citations?fields=title,year,externalIds&limit=100'})
def get(it):
 name,url=it
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read();path=Path(name+('.pdf' if name[0].isdigit() else '.response'));path.write_bytes(data)
  if name[0].isdigit():
   import pymupdf
   d=pymupdf.open(path);Path(name+'.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return name,url,'OK'
 except Exception as e:return name,url,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:r=list(e.map(get,urls.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for x in r:f.write('\n- '+' | '.join(x)+' (2026-10-12)\n')
print(r)
