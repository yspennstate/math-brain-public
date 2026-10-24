import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime
P=pathlib.Path(__file__).parent;q=urllib.parse.quote
U={
'arxiv_recent':'https://export.arxiv.org/api/query?search_query='+q('all:"dimer" AND (all:"height" OR all:"correlators")')+'&sortBy=submittedDate&sortOrder=descending&max_results=60',
'arxiv_chaos':'https://export.arxiv.org/api/query?search_query='+q('all:"dimer" AND all:"chaos"')+'&max_results=20',
'crossref_dubedat':'https://api.crossref.org/works?query.bibliographic='+q('Dubedat Dimers analytic torsion electric correlators')+'&rows=10',
'openalex_retry':'https://api.openalex.org/works?search='+q('Dimers families Cauchy Riemann operators')+'&per_page=10',
'semantic_direct':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1110.2808?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
}
def f(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40);b=r.read();(P/(k+'.json')).write_bytes(b);out=f'{k}: {r.status}, {len(b)} bytes'
 except Exception as e:out=f'{k}: {e}'
 return {'date':str(datetime.date.today()),'service':k,'url':u,'result':out}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(lambda kv:f(*kv),U.items()):
  with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(r)+'\n')
  print(r['result'])
