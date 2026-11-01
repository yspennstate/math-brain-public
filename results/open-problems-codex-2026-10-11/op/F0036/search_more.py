import requests,pathlib,json,concurrent.futures,pymupdf
jobs=[('citing_published','https://api.openalex.org/works',{'filter':'cites:W2121110727','per-page':200}),('citing_arxiv','https://api.openalex.org/works',{'filter':'cites:W4300525659','per-page':200}),('crossref_net','https://api.crossref.org/works',{'query.title':'Brownian net','rows':50}),('semantic_search','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'Brownian net','limit':100,'fields':'title,year,externalIds,abstract'}),('openalex_exact','https://api.openalex.org/works',{'search':'"potential most recent common ancestors"','per-page':50}),('arxiv_retry','https://export.arxiv.org/api/query',{'search_query':'ti:"Brownian net"','max_results':50}),('special_times','https://arxiv.org/pdf/2512.10761',{}),('universality','https://arxiv.org/pdf/2401.09370',{}),('special_points','https://arxiv.org/pdf/0806.2326',{})]
def run(j):
 n,u,p=j
 try:
  r=requests.get(u,params=p,timeout=50); info=dict(service=n,url=r.url,status=r.status_code,date='2026-10-12',bytes=len(r.content))
  if r.status_code==200 and r.content.startswith(b'%PDF'):
   pathlib.Path(n+'.pdf').write_bytes(r.content); d=pymupdf.open(stream=r.content,filetype='pdf'); pathlib.Path(n+'.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf8'); info['pages']=len(d)
  else: pathlib.Path(n+'.response').write_text(r.text,encoding='utf8')
  return info
 except Exception as e: return dict(service=n,url=u,query=p,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex: out=list(ex.map(run,jobs))
p=pathlib.Path('search_log.json'); old=json.loads(p.read_text(encoding='utf8')); p.write_text(json.dumps(old+out,indent=2),encoding='utf8')
for x in out: print(json.dumps(x))
