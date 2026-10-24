import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime
q='Noise sensitivity in bootstrap percolation'
urls={
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"bootstrap percolation" AND all:"noise"')+'&max_results=50',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote(q)+'&per-page=30',
'crossref':'https://api.crossref.org/works?query.title='+urllib.parse.quote(q)+'&rows=15',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1509.08454?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('bootstrap percolation noise sensitivity'),
'openalex_regular':'https://api.openalex.org/works?search='+urllib.parse.quote('bootstrap percolation random regular noise sensitivity')+'&per-page=30',
}
def get(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'}),timeout=45); b=r.read();pathlib.Path(k+'.json' if k!='arxiv' else k+'.xml').write_bytes(b)
  return k,u,'OK',b.decode()[:180] if k=='arxiv' else ''
 except Exception as e:return k,u,str(e),''
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(lambda kv:get(*kv),urls.items()))
pathlib.Path('search_log.json').write_text(json.dumps({'date':'2026-10-12','results':results},indent=2),encoding='utf8')
for x in results:print(x)
for k in ['openalex','openalex_regular','crossref','semantic','github']:
 p=pathlib.Path(k+'.json')
 if not p.exists():continue
 d=json.loads(p.read_text())
 if k.startswith('openalex'):
  for w in d['results']:print(k,w['id'],w['publication_year'],w['title'],w.get('doi'))
 elif k=='crossref':
  for w in d['message']['items']:print(k,w.get('title'),w.get('DOI'))
 elif k=='semantic':print(json.dumps(d,indent=2))
 else:print('github total',d.get('total_count'))
