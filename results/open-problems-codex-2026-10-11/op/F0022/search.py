import requests, pathlib, concurrent.futures, json, datetime
root=pathlib.Path('.')
queries=[('arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"percolation" AND (all:"cluster number" OR all:"free energy" OR all:"cluster density")','max_results':30}),('openalex','https://api.openalex.org/works',{'search':'percolation mean number clusters singularity','per-page':30}),('crossref','https://api.crossref.org/works',{'query':'percolation number clusters singularity critical triangular','rows':30}),('semantic_scholar','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'percolation number clusters singularity','limit':30,'fields':'title,authors,year,externalIds,url,abstract'}),('github','https://api.github.com/search/repositories',{'q':'percolation cluster singularity','per_page':30}),('openalex_source','https://api.openalex.org/works',{'search':'Planar percolation with a glimpse of Schramm Loewner evolution','per-page':5})]
def run(x):
 name,url,params=x
 try:
  r=requests.get(url,params=params,timeout=50); (root/(name+'.response')).write_text(r.text,encoding='utf-8'); return {'service':name,'url':r.url,'status':r.status_code,'date':'2026-10-12','file':name+'.response'}
 except Exception as e: return {'service':name,'url':url,'params':params,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(run,queries))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results: print(r)
for name in ['openalex','crossref','semantic_scholar','openalex_source']:
 try:
  d=json.loads((root/(name+'.response')).read_text(encoding='utf-8')); rows=d.get('results',d.get('data',d.get('message',{}).get('items',[])))
  for x in rows: print(name,x.get('id'),x.get('publication_year',x.get('year')),x.get('title'),x.get('DOI',x.get('doi')))
 except Exception as e: print(name,e)
