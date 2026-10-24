import urllib.request,urllib.parse,pathlib,json,concurrent.futures
q=urllib.parse.quote
items=[('openalex_retry','https://api.openalex.org/works?search='+q('"Forward Brownian motion"')+'&per_page=10'),('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1214/13-EJP3343'),('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1302.6958?fields=title,year,authors,externalIds,citations.title,citations.year,citations.abstract,citations.externalIds'),('arxiv_decomp','https://export.arxiv.org/api/query?search_query='+q('all:"decomposable" AND all:"Brownian"')+'&max_results=30'),('arxiv_authors','https://export.arxiv.org/api/query?search_query='+q('au:Burdzy AND au:Scheutzow')+'&max_results=40'),('crossref_compat','https://api.crossref.org/works?query='+q('"backward Brownian" "forward Brownian"')+'&rows=20'),('github_decomp','https://api.github.com/search/repositories?q='+q('Brownian decomposable'))]
def run(it):
 name,url=it
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research/1.0','Accept':'application/json' if 'arxiv' not in name else '*/*'}),timeout=40) as r: t=r.read().decode(); code=r.status
 except Exception as e:t=str(e);code='ERROR'
 pathlib.Path('search_'+name+'.txt').write_text(t,encoding='utf8')
 print(name,code,t[:160] if code=='ERROR' else len(t),flush=True)
 return dict(service=name,url=url,status=code,date='2026-10-12',file='search_'+name+'.txt')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(run,items))
p=pathlib.Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+out,indent=2),encoding='utf8')
