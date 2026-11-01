import urllib.request,urllib.parse,json,pathlib,concurrent.futures
q=urllib.parse.quote
jobs=[('arxiv_target.xml','https://export.arxiv.org/api/query?search_query='+q('all:"coagulation" AND (all:"relaxation" OR all:"spectral gap" OR all:"linear polymers")')+'&max_results=50'),('openalex_retry.json','https://api.openalex.org/works?search='+q('coagulation fragmentation')+'&per_page=20'),('openalex_source.json','https://api.openalex.org/works?search='+q('Coagulation fragmentation relaxation Aldous')+'&per_page=10'),('openalex_hingant.json','https://api.openalex.org/works/https://doi.org/10.1214/18-PS321'),('semantic_retry.json','https://api.semanticscholar.org/graph/v1/paper/search/bulk?query='+q('"coagulation" "mixing"')+'&fields=title,year,authors,externalIds,abstract'),('crossref_target.json','https://api.crossref.org/works?query='+q('stochastic coagulation fragmentation spectral gap')+'&rows=30')]
def fetch(x):
 name,url=x
 try:
  b=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'P0211 research contact not supplied'}),timeout=40).read(); pathlib.Path(name).write_bytes(b); out={'date':'2026-10-11','file':name,'url':url,'bytes':len(b),'status':'OK'}
 except Exception as e: out={'date':'2026-10-11','file':name,'url':url,'status':str(e)}
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rows=list(ex.map(fetch,jobs))
with open('search_log.jsonl','a',encoding='utf8') as f:
 for r in rows: f.write(json.dumps(r)+'\n')
print(json.dumps(rows,indent=2))
