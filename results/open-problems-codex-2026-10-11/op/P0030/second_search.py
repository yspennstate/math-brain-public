import urllib.request,urllib.parse,pathlib,json,concurrent.futures
queries=[('crossref_kakutani','https://api.crossref.org/works?query.title='+urllib.parse.quote('On equivalence of infinite product measures')+'&rows=3'),('crossref_thorisson','https://api.crossref.org/works?query.title='+urllib.parse.quote('Transforming random elements and shifting random fields')+'&rows=3'),('arxiv_hellinger_fbm','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"forward Brownian" AND (all:Kakutani OR all:Hellinger OR all:"absolute continuity")')+'&max_results=20')]
def get(it):
 n,u=it
 try:
  with urllib.request.urlopen(u,timeout=40) as r:s=r.status;t=r.read().decode()
 except Exception as e:s='ERROR';t=str(e)
 pathlib.Path('second_search_'+n+'.txt').write_text(t,encoding='utf8')
 return dict(date='2026-10-12',service=n,url=u,status=s,file='second_search_'+n+'.txt')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(get,queries))
pathlib.Path('second_search_log.json').write_text(json.dumps(a,indent=2),encoding='utf8');print(json.dumps(a,indent=2))
