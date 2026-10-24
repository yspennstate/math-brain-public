import urllib.request,urllib.parse,pathlib,json,datetime,concurrent.futures
P=pathlib.Path(__file__).parent;q=urllib.parse.quote
U={
'jsw_pdf':'https://arxiv.org/pdf/1806.02118',
'openalex_kenyon_doi':'https://api.openalex.org/works/https://doi.org/10.1090/pcms/016/04',
'openalex_cites_kenyon_doi':'https://api.openalex.org/works?filter='+q('cites:https://doi.org/10.1090/pcms/016/04')+'&per-page=30',
'semantic_kenyon_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0910.3129/citations?fields=title,authors,year,externalIds&limit=100',
'crossref_vertex':'https://api.crossref.org/works?query.bibliographic='+q('square lattice dimer vertex operators electric correlations')+'&rows=20',
'crossref_cr':'https://api.crossref.org/works?query.title='+q('Dimers and families of Cauchy Riemann operators')+'&rows=5',
}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();(P/(k+('.pdf' if k.endswith('pdf') else '.json'))).write_bytes(b);out=f'{k}: {r.status}, {len(b)} bytes'
 except Exception as e:out=f'{k}: {e}'
 return {'date':str(datetime.date.today()),'service':k,'url':u,'result':out}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(lambda kv:f(*kv),U.items()):
  with (P/'SEARCH_LOG.jsonl').open('a',encoding='utf8') as h:h.write(json.dumps(r)+'\n')
  print(r['result'])
