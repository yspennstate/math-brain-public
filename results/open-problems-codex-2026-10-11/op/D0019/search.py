import urllib.request, urllib.parse, pathlib, json, concurrent.futures,datetime
queries=[('arxiv','http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Brownian sheet" AND (all:projection OR all:Marstrand)','max_results':40})),('arxiv_https','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Brownian sheet" AND all:projection','max_results':40})),('openalex','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian sheet projections','per-page':40})),('openalex_source','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Slices of Brownian Sheet New Results and Open Problems','per-page':5})),('crossref','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Brownian sheet zero set projection Marstrand','rows':30})),('semantic_scholar','https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Brownian sheet projection','limit':40,'fields':'title,authors,year,externalIds,url,abstract'})),('github','https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Brownian sheet projection','per_page':30}))]
def fetch(x):
 name,url=x
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0019-mathematics-literature-check/1.0'})
  r=urllib.request.urlopen(req,timeout=45); b=r.read(); pathlib.Path(name+'.response').write_bytes(b); msg=f'{name}: HTTP {r.status}, {len(b)} bytes'
 except Exception as e: msg=f'{name}: {type(e).__name__}: {e}';pathlib.Path(name+'.response').write_text(msg,encoding='utf8')
 return name,url,msg
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 results=list(pool.map(fetch,queries))
with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,msg in results: f.write(f'\n- 2026-10-12 `{name}`: {url}\n  Outcome: {msg}. Raw response: `{name}.response`.\n'); print(msg)
for name in ['openalex','openalex_source','crossref','semantic_scholar','github']:
 try:
  d=json.loads(pathlib.Path(name+'.response').read_text(encoding='utf8'))
  items=d.get('results',d.get('data',d.get('items',d.get('message',{}).get('items',[]))))
  print('\n',name)
  for v in items: print(v.get('id',''),v.get('year',v.get('publication_year','')),v.get('title',v.get('display_name',v.get('full_name',''))),v.get('doi',v.get('URL','')))
 except Exception: pass
