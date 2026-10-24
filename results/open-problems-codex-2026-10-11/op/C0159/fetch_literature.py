import urllib.request, urllib.parse, concurrent.futures, json, pathlib, datetime
root=pathlib.Path('.')
jobs={
'source': 'https://projecteuclid.org/journals/probability-surveys/volume-3/issue-none/Uniqueness-and-non-uniqueness-in-percolation-theory/10.1214/154957806000000096.pdf',
'bell_pdf':'https://arxiv.org/pdf/2509.10631',
'bell_abs':'https://arxiv.org/abs/2509.10631',
'arxiv':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"cluster repulsion"','max_results':30}),
'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'cluster repulsion nonunimodular','per-page':30}),
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/154957806000000096',
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'cluster repulsion percolation','rows':30}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'cluster repulsion','limit':30,'fields':'title,year,authors,url,abstract'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'cluster repulsion percolation'})}
def fetch(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'C0159-Mathematical-Research/1.0'}),timeout=45); b=r.read(); root.joinpath(k+('.pdf' if k in ['source','bell_pdf'] else '.txt')).write_bytes(b); out={'service':k,'url':u,'date':'2026-10-11','status':r.status,'bytes':len(b)}
 except Exception as e: out={'service':k,'url':u,'date':'2026-10-11','error':str(e)}
 with root.joinpath('search_log.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(out)+'\n')
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for out in ex.map(lambda kv:fetch(*kv),jobs.items()): print(json.dumps(out))
