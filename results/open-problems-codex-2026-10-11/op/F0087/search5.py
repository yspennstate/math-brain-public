import urllib.request,urllib.parse,pathlib,json,datetime,concurrent.futures
P=pathlib.Path(__file__).parent;q=urllib.parse.quote
U={
'semantic_kenyon_citations2':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0910.3129/citations?fields=title,authors,year,externalIds&limit=100&offset=100',
'semantic_dubedat_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1110.2808/citations?fields=title,authors,year,externalIds&limit=100',
'semantic_chaos_search':'https://api.semanticscholar.org/graph/v1/paper/search?query='+q('dimer imaginary multiplicative chaos')+'&limit=20&fields=title,authors,year,externalIds',
'arxiv_targeted_alt':'https://arxiv.org/api/query?search_query='+q('all:"dimer" AND all:"electric"')+'&max_results=20',
'crossref_pinson':'https://api.crossref.org/works?query.title='+q('Rotational invariance and discrete analyticity in the 2d dimer model')+'&rows=3',
}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();(P/(k+'.json')).write_bytes(b);out=f'{k}: {r.status}, {len(b)} bytes'
 except Exception as e:out=f'{k}: {e}'
 return {'date':str(datetime.date.today()),'service':k,'url':u,'result':out}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(lambda kv:f(*kv),U.items()):
  with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(r)+'\n')
  print(r['result'])
