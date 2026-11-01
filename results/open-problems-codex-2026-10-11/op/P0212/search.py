import urllib.request, urllib.parse, pathlib, concurrent.futures, json, datetime
root=pathlib.Path(__file__).resolve().parent
queries={
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"branching coalescing" AND (all:"low density" OR all:genealogy OR all:genealogical)')+'&max_results=30',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('low density branching coalescing random walk genealogy')+'&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('low density coalescing branching random walk')+'&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('branching coalescing genealogy')+'&limit=20&fields=title,authors,year,url,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('branching coalescing random walk'),
 'ising':'https://www.stat.berkeley.edu/~aldous/Talks/persi-ising.pdf',
 'pillai':'https://www.stat.berkeley.edu/~aldous/Research/OP/pillai-smith.pdf',
 'athreya':'https://www.isid.ac.in/~statmath/eprints/2003/isid200322.pdf',
 'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('The low-density limit of coalescing branching random walk')+'&per-page=10',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0212-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (root/(name+('.pdf' if name in ['ising','pillai','athreya'] else '.txt'))).write_bytes(data)
  state='OK '+str(len(data))+' bytes'
 except Exception as e: state=repr(e)
 return name,url,state
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,queries.items()))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Searches on 2026-10-11\n')
 for name,url,state in results:
  f.write(f'- {name}: {url}\n  Result: {state}\n')
  print(name,state)
for name in ['openalex','openalex_source','crossref','semantic','github']:
 p=root/(name+'.txt')
 if not p.exists(): continue
 try:
  obj=json.loads(p.read_text(encoding='utf8'))
  rows=obj.get('results',obj.get('data',obj.get('items',obj.get('message',{}).get('items',[]))))
  print('\n'+name)
  for x in rows: print(x.get('id',x.get('DOI','')),x.get('publication_year',x.get('year','')),x.get('title',x.get('full_name','')))
 except Exception as e: print(e)
