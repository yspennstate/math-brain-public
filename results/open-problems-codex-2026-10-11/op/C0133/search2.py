import urllib.request,urllib.parse,json,concurrent.futures
from pathlib import Path
qs={
'openalex_citing_published':'https://api.openalex.org/works?filter=cites:W2962897620&per-page=200',
'openalex_citing_arxiv':'https://api.openalex.org/works?filter=cites:W2276429711&per-page=200',
'arxiv_zeroone':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"excited random walks" AND (all:"zero-one" OR all:"non-transient" OR all:"non-ballistic")')+'&max_results=50',
'crossref_excited':'https://api.crossref.org/works?query.title='+urllib.parse.quote('excited random walk')+'&rows=50',
'paper_exchangeable':'https://arxiv.org/pdf/1311.6158',
'openalex_lln':'https://api.openalex.org/works?search='+urllib.parse.quote('excited random walk law large numbers')+'&per-page=40'}
def f(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'C0133-literature-audit'}),timeout=35);b=r.read();ext='.pdf' if k.startswith('paper') else ('.xml' if k.startswith('arxiv') else '.json');Path(k+ext).write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda x:f(*x),qs.items()))
Path('search_log_2.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':r},indent=2));print(r)
