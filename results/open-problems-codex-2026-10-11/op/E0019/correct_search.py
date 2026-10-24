from pathlib import Path
import urllib.request,urllib.parse,json
jobs={
'openalex_correct_doi':'https://api.openalex.org/works/https://doi.org/10.5802/afst.1468',
'openalex_doi_search':'https://api.openalex.org/works?filter=doi:https://doi.org/10.5802/afst.1468',
'semantic_doi':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.5802/afst.1468?fields=title,year,citations.title,citations.year,citations.externalIds',
'crossref_regular_exact':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Regularity of the stationary density for systems with fast random switching')+'&rows=3'}
import concurrent.futures
def f(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'E0019 mathematical research'}),timeout=35) as h:b=h.read()
  Path(k+'.json').write_bytes(b);return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(f,jobs.items()))
with open('LITERATURE.md','a',encoding='utf8') as h:
 for k,u,s,n in r:h.write(f'\n- 2026-10-12 {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(r,indent=2))
for k in ['openalex_correct_doi','openalex_doi_search']:
 p=Path(k+'.json')
 if p.exists():
  j=json.loads(p.read_bytes()); w=j if 'id' in j else j['results'][0];wid=w['id'].split('/')[-1]
  url='https://api.openalex.org/works?filter=cites:'+wid+'&per_page=100'
  try:
   with urllib.request.urlopen(url,timeout=35) as h:b=h.read()
   Path('openalex_confirmed_citing.json').write_bytes(b);out='OK'
  except Exception as e:out=str(e)
  with open('LITERATURE.md','a',encoding='utf8') as h:h.write(f'\n- 2026-10-12 OpenAlex verified-source citations: `{url}` — {out}.\n')
  print(wid,out);break
