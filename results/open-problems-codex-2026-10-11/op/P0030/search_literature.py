import urllib.request,urllib.parse,json,concurrent.futures,pathlib,datetime
q=urllib.parse.quote
queries=[('arxiv_http','http://export.arxiv.org/api/query?search_query='+q('all:"forward Brownian motion"')+'&max_results=30'),('arxiv_https','https://export.arxiv.org/api/query?search_query='+q('all:"forward Brownian motion"')+'&max_results=30'),('openalex_title','https://api.openalex.org/works?search='+q('Forward Brownian motion')+'&per-page=30'),('crossref','https://api.crossref.org/works?query.title='+q('Forward Brownian motion')+'&rows=20'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('Forward Brownian motion')+'&limit=30&fields=title,authors,year,abstract,externalIds,url'),('github','https://api.github.com/search/repositories?q='+q('"forward Brownian"')),('openalex_compat','https://api.openalex.org/works?search='+q('decomposable forward backward Brownian motion')+'&per-page=20')]
def run(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read().decode('utf8'); code=r.status
 except Exception as e: data=str(e); code='ERROR'
 pathlib.Path('search_'+name+'.txt').write_text(data,encoding='utf8')
 return {'service':name,'url':url,'status':code,'date':'2026-10-12','file':'search_'+name+'.txt'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(run,queries))
pathlib.Path('search_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for x in out: print(x)
