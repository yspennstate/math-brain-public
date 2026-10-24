import urllib.request,json,pathlib,concurrent.futures,xml.etree.ElementTree as E
q={
'openalex_source':'https://api.openalex.org/works?filter=doi:10.1214/08-AIHP167&per-page=5',
'openalex_search_retry':'https://api.openalex.org/works?search=Poisson%20matching&per-page=30',
'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867/citations?limit=100&fields=title,authors,year,abstract,url',
'arxiv_tail':'https://export.arxiv.org/api/query?search_query=all:matching%20AND%20all:Poisson%20AND%20(all:tail%20OR%20all:stable)&max_results=100',
'crossref_source':'https://api.crossref.org/works?query.title=Poisson%20matching&query.author=Holroyd&rows=5',
'minimal_pdf':'https://arxiv.org/pdf/2012.07129',
'pwit_pdf':'https://arxiv.org/pdf/1708.04519',
'hyperuniform_pdf':'https://arxiv.org/pdf/1810.00265'}
def f(k,u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0081-research'}),timeout=40) as r: b=r.read()
  ext='.pdf' if k.endswith('_pdf') else '.xml' if k.startswith('arxiv') else '.json'
  pathlib.Path(k+ext).write_bytes(b)
  if ext=='.pdf':
   import pymupdf
   d=pymupdf.open(k+ext);pathlib.Path(k+'.txt').write_text('\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return dict(service=k,url=u,date='2026-10-11',file=k+ext,bytes=len(b))
 except Exception as e:return dict(service=k,url=u,date='2026-10-11',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: a=list(ex.map(lambda kv:f(*kv),q.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
