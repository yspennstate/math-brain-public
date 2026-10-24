import urllib.request,urllib.parse,concurrent.futures,json
from pathlib import Path
urls={'bf.pdf':'https://arxiv.org/pdf/0804.3035','hks.pdf':'https://arxiv.org/pdf/1911.04392','arxiv_hks.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Discrete variants of Brunn Minkowski"')+'&max_results=5','arxiv_gt.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"TASEP" AND all:"Gelfand"')+'&max_results=15','petrov_directory.html':'https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/'}
def f(it):
 k,u=it
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();Path(k).write_bytes(b);return[k,u,r.status,len(b)]
 except Exception as e:return[k,u,str(e)]
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(f,urls.items()));Path('search_log_3.json').write_text(json.dumps(r,indent=2));print(r)
import pymupdf
if Path('bf.pdf').exists():
 d=pymupdf.open('bf.pdf');s='\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));Path('bf.txt').write_text(s,encoding='utf8')
 for term in ['Proposition 2.','Proposition 3.','TASEP','Poisson','Gelfand']:
  p=s.find(term);print(term,s[max(0,p-200):p+2500])
