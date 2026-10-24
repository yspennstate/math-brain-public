exec(open('search.py',encoding='utf8').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
'citing_book':'https://api.openalex.org/works?filter=cites:W2121110727&per-page=200',
'citing_arxiv':'https://api.openalex.org/works?filter=cites:W4300525659&per-page=200',
'arxiv_bubble':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"bubble hypothesis"','max_results':100}),
'openalex_backbone':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"Brownian net" backbone','per-page':100}),
'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1506.00724/citations?limit=100&fields=title,year,authors,abstract,externalIds',
'special_times':'https://arxiv.org/pdf/2512.10761',
'universality':'https://arxiv.org/pdf/2401.09370',
'special_points':'https://arxiv.org/pdf/0806.2326',
}
def get(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'probability-research/1.0'}),timeout=45) as r: data=r.read()
  pdf=data.startswith(b'%PDF')
  fn=name+('.pdf' if pdf else '.xml' if name.startswith('arxiv') else '.json')
  (P/fn).write_bytes(data)
  if pdf:
   import pymupdf
   doc=pymupdf.open(P/fn)
   (P/(name+'.txt')).write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  outcome=f'HTTP 200, {len(data)} bytes, {fn}'
 except Exception as e: outcome=str(e)
 return {'service':name,'url':url,'date':'2026-10-12','outcome':outcome}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: results=list(ex.map(get,queries.items()))
(P/'follow_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(r)
for name in ['citing_book','citing_arxiv','openalex_backbone']:
 try:
  data=json.loads((P/(name+'.json')).read_text(encoding='utf8'))
  print(name,'count',data['meta']['count'])
  for x in data['results']: print(x['publication_year'],x['title'],x['doi'])
 except Exception: pass
