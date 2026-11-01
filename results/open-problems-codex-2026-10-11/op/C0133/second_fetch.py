import urllib.request,urllib.parse,json,concurrent.futures
from pathlib import Path
qs={
'zerner_openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('A non-ballistic law of large numbers for random walks in iid random environment')+'&per-page=3',
'zerner_arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"non-ballistic" AND au:Zerner')+'&max_results=10',
'hewitt_crossref':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Symmetric measures on Cartesian products')+'&rows=3'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();Path(k+('.xml' if 'arxiv' in k else '.json')).write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_search_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':rs},indent=2));print(rs)
