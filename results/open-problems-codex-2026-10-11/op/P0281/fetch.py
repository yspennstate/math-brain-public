import urllib.request, urllib.parse, concurrent.futures, json, datetime
from pathlib import Path
base='https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf'
q='TASEP log concavity'
urls={'source.pdf':base,'arxiv.xml':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:TASEP AND (all:"log concavity" OR all:log-concavity)')+'&max_results=30','openalex.json':'https://api.openalex.org/works?search='+urllib.parse.quote(q)+'&per-page=30','crossref.json':'https://api.crossref.org/works?query='+urllib.parse.quote(q)+'&rows=30','semantic.json':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote(q)+'&limit=30&fields=title,authors,year,abstract,url','github.json':'https://api.github.com/search/repositories?q='+urllib.parse.quote('TASEP log concavity'),'openalex_source.json':'https://api.openalex.org/works?search='+urllib.parse.quote('All roads to KPZ universality')+'&per-page=10'}
def get(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45); b=r.read(); Path(k).write_bytes(b); return (k,u,r.status,len(b))
 except Exception as e:return(k,u,str(e))
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(lambda kv:get(*kv),urls.items()))
Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(r)
try:
 import pymupdf
 doc=pymupdf.open('source.pdf'); text='\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)); Path('source.txt').write_text(text,encoding='utf8');print(text)
except Exception as e: print('PDF extraction:',e)
