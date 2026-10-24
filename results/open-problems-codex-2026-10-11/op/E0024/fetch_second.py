import urllib.request,urllib.parse,json,pathlib,concurrent.futures
queries={
'openalex_symmetric_H':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"symmetric Lévy" "Hunt"','per-page':30}),
'crossref_kakutani':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'Kakutani equivalence infinite product measures 1948','rows':5}),
'openalex_absolute_H':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'"Hunt" "absolute continuity" "Lévy"','per-page':30})}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'ResearchMath/1.0'}),timeout=35) as r: data=r.read()
  pathlib.Path(k+'.raw').write_bytes(data);return {'date':'2026-10-12','service_query':k,'url':u,'file':k+'.raw','status':'ok'}
 except Exception as e:return {'date':'2026-10-12','service_query':k,'url':u,'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: res=list(ex.map(get,queries.items()))
p=pathlib.Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+res,indent=2));print(res)
for k in queries:
 p=pathlib.Path(k+'.raw')
 if not p.exists():continue
 d=json.loads(p.read_text());print(k)
 for r in d.get('results',d.get('message',{}).get('items',[])):
  print(r.get('title'),r.get('doi',r.get('DOI')),r.get('publication_year'))
