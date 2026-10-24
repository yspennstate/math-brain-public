import urllib.request, urllib.parse, json, pathlib, concurrent.futures
P=pathlib.Path(__file__).resolve().parent
jobs={
 'openalex_title':'https://api.openalex.org/works?search=Operator%20limits%20of%20random%20matrices&per-page=5',
 'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1804.06953',
 'arxiv_nested':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"nested" AND all:"beta" AND all:"ensembles"')+'&max_results=30',
 'arxiv_corners':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"beta" AND all:"corners"')+'&max_results=30',
 'arxiv_laguerre':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Laguerre" AND all:"minors"')+'&max_results=20',
 'crossref_corners':'https://api.crossref.org/works?query='+urllib.parse.quote('beta corners process tridiagonal nesting')+'&rows=15',
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds',
}
def fetch(name,url):
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'D0040-research/1.0'}),timeout=40) as r: data=r.read()
  (P/(name+'.response')).write_bytes(data); result='OK '+str(len(data))
  if name.startswith('openalex'):
   j=json.loads(data); works=j.get('results',[j]); print(name,[(w.get('id'),w.get('title')) for w in works],flush=True)
   for w in works:
    if 'operator limits of random matrices' in w.get('title','').lower() and w.get('id'):
     wid=w['id'].split('/')[-1]
     fetch('openalex_citing','https://api.openalex.org/works?filter=cites:'+wid+'&per-page=100')
 except Exception as e: result='ERROR '+repr(e)
 with (P/'search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps({'date':'2026-10-12','service':name,'url':url,'result':result})+'\n')
 print(name,result,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: list(ex.map(lambda x:fetch(*x),jobs.items()))
