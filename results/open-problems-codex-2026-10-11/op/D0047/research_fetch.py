import pathlib,urllib.request,urllib.parse,json,concurrent.futures,datetime
p=pathlib.Path('.')
queries={
'source':'https://arxiv.org/pdf/1804.06953',
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Brownian carousel" AND all:Painleve')+'&max_results=30',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('Brownian carousel Painleve')+'&per-page=30',
'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('Operator limits of random matrices')+'&per-page=5',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('Brownian carousel Painleve')+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Brownian carousel Painleve')+'&limit=20&fields=title,year,authors,url,abstract',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('Brownian carousel Painleve')}
def fetch(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'D0047-math-research/1.0'}),timeout=45); b=r.read(); (p/(k+('.pdf' if k=='source' else '.json'))).write_bytes(b); return k,len(b),'OK'
 except Exception as e: return k,0,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(lambda kv:fetch(*kv),queries.items()))
(p/'search_log.json').write_text(json.dumps({'date':'2026-10-12','queries':queries,'results':results},indent=2),encoding='utf8')
print(results)
try:
 import pymupdf
 doc=pymupdf.open('source.pdf'); (p/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8'); print('PDF extracted',len(doc))
except Exception as e: print('extract',e)
