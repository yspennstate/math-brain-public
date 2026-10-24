import urllib.request,urllib.parse,json,concurrent.futures,time
from pathlib import Path
queries={
'arxiv': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Poissonian" AND all:"polymer"','start':0,'max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),
'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian polymers Poissonian environment','per-page':50}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Brownian polymers Poissonian environment','rows':30}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Brownian polymers Poissonian environment','limit':30,'fields':'title,authors,year,externalIds,url,abstract'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Brownian polymer Poissonian'}),
'arxiv_http':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Poissonian" AND all:"polymer"','max_results':30})}
def get(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'E0112-research/1.0'})
  r=urllib.request.urlopen(req,timeout=50);b=r.read();Path('search_'+k+'.txt').write_bytes(b)
  return k,u,r.status,len(b),None
 except Exception as e:return k,u,None,0,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 out=list(pool.map(lambda kv:get(*kv),queries.items()))
Path('search_log.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for row in out:print(row)
if Path('search_openalex.txt').exists():
 j=json.loads(Path('search_openalex.txt').read_text())
 for x in j.get('results',[]):print('OA',x['id'],x['publication_year'],x['title'],x.get('doi'),x.get('cited_by_count'))
if Path('search_crossref.txt').exists():
 for x in json.loads(Path('search_crossref.txt').read_text())['message']['items']:print('CR',x.get('published',{}),x.get('title'),x.get('DOI'))
