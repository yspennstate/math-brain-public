import json,pathlib,urllib.request,urllib.parse,concurrent.futures
p=pathlib.Path('.')
d=json.loads((p/'crossref.json').read_text())
for x in d['message']['items'][:20]: print(x.get('title'),x.get('DOI'))
print((p/'arxiv.json').read_text())
qs={
'arxiv_carousel':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"carousel" AND (all:"Painlevé" OR all:"Painleve")')+'&max_results=30',
'arxiv_gap':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"sine" AND all:"Painleve"')+'&max_results=40',
'openalex_retry':'https://api.openalex.org/works?search=Brownian%20carousel&per_page=25',
'openalex_source_retry':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1804.06953',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,citations.title,citations.year,citations.externalIds',
'crossref_target':'https://api.crossref.org/works?query='+urllib.parse.quote('Painleve Brownian carousel bulk gap generator')+'&rows=30'}
def f(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (mathematics research)'}),timeout=35).read(); (p/(k+'.json')).write_bytes(b); return k,'OK',len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
(p/'search_log_2.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':r},indent=2));print(r)
