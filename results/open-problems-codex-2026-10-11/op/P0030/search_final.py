import urllib.request,urllib.parse,pathlib,json,concurrent.futures
q=urllib.parse.quote
items=[('openalex_citing_filter','https://api.openalex.org/works?filter=references.doi:'+q('https://doi.org/10.1007/s00440-013-0524-x')+'&per-page=100'),('openalex_citing_search','https://api.openalex.org/works?search='+q('1302.6958')+'&per-page=50'),('semantic_citations','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1302.6958/citations?fields=title,year,abstract,externalIds&limit=100'),('crossref_exact','https://api.crossref.org/works/10.1007/s00440-013-0524-x'),('arxiv_stationary','https://export.arxiv.org/api/query?search_query='+q('all:"forward Brownian" AND (all:stationary OR all:coupling)')+'&max_results=30'),('arxiv_backward','https://export.arxiv.org/api/query?search_query='+q('all:"backward Brownian motion"')+'&max_results=50')]
def run(it):
 name,url=it
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research/1.0'}),timeout=35) as r:t=r.read().decode();code=r.status
 except Exception as e:t=str(e);code='ERROR'
 pathlib.Path('search_'+name+'.txt').write_text(t,encoding='utf8');print(name,code, t[:160] if code=='ERROR' else len(t),flush=True)
 return dict(service=name,url=url,status=code,date='2026-10-12',file='search_'+name+'.txt')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(run,items))
p=pathlib.Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+out,indent=2),encoding='utf8')
