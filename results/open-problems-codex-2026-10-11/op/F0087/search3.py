import urllib.request,urllib.parse,pathlib,json,datetime,concurrent.futures
P=pathlib.Path(__file__).parent;q=urllib.parse.quote
U={
'dubedat_source':'https://arxiv.org/src/1110.2808',
'arxiv_targeted':'https://export.arxiv.org/api/query?search_query='+q('all:"electric correlators"')+'&max_results=20',
'arxiv_imaginary':'https://export.arxiv.org/api/query?search_query='+q('all:"imaginary multiplicative chaos"')+'&max_results=40',
'crossref_chaos':'https://api.crossref.org/works?query.bibliographic='+q('dimer height imaginary multiplicative chaos')+'&rows=15',
'crossref_kenyon':'https://api.crossref.org/works?query.bibliographic='+q('Kenyon Lectures on dimers')+'&rows=5',
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2120491439&per-page=30',
'openalex_source_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.0910.3129',
'github_height':'https://api.github.com/search/repositories?q='+q('dimer height imaginary chaos'),
}
def f(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0087 research'}),timeout=40);b=r.read();(P/(k+('.tar' if k.endswith('source') else '.json'))).write_bytes(b);out=f'{k}: {r.status}, {len(b)} bytes'
 except Exception as e:out=f'{k}: {e}'
 return {'date':str(datetime.date.today()),'service':k,'url':u,'result':out}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(lambda kv:f(*kv),U.items()):
  with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(r)+'\n')
  print(r['result'])
