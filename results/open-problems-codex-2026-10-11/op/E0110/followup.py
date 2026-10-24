import json,urllib.request,urllib.parse,concurrent.futures,pathlib
j=json.load(open('crossref_retry.txt',encoding='utf8'))
for w in j['message']['items']:print(w.get('title'),w.get('DOI'),w.get('published',{}))
Q=urllib.parse.quote
urls={
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1007/s11134-019-09610-5',
'openalex_doi_filter':'https://api.openalex.org/works?filter=doi:'+Q('https://doi.org/10.1007/s11134-019-09610-5'),
'semantic_doi_citations':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11134-019-09610-5/citations?fields=title,year,authors,externalIds&limit=100',
'arxiv_soft':'https://export.arxiv.org/api/query?search_query='+Q('all:"soft reflection" OR all:"OConnell-Yor" OR (all:"O\'Connell-Yor" AND all:"convergence")')+'&max_results=60',
'arxiv_dimension':'https://export.arxiv.org/api/query?search_query='+Q('ti:"reflected Brownian" AND (all:"dimension" OR all:"relaxation")')+'&max_results=40'}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read()
  pathlib.Path(k+'.txt').write_bytes(b);s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 print(k,s,flush=True)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
 for k,u,s in p.map(get,urls.items()):
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: {u}\n  {s}\n')
