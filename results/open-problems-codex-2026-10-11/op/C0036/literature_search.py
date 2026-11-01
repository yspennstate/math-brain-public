import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parent
queries=[
 ('arxiv','Fuglede Kadison determinantal','https://export.arxiv.org/api/query?search_query=all:%22Fuglede%22+AND+all:%22determinantal%22&max_results=40'),
 ('arxiv','Lyons stochastic domination determinantal','https://export.arxiv.org/api/query?search_query=all:%22determinantal%22+AND+all:%22domination%22&max_results=60&sortBy=submittedDate&sortOrder=descending'),
 ('OpenAlex','Fuglede Kadison determinantal','https://api.openalex.org/works?search=Fuglede%20Kadison%20determinantal&per-page=40'),
 ('OpenAlex','Determinantal probability basic properties conjectures','https://api.openalex.org/works?search=Determinantal%20probability%20basic%20properties%20conjectures&per-page=5'),
 ('Crossref','Fuglede Kadison determinantal','https://api.crossref.org/works?query=Fuglede%20Kadison%20determinantal&rows=30'),
 ('SemanticScholar','Fuglede Kadison determinantal','https://api.semanticscholar.org/graph/v1/paper/search?query=Fuglede%20Kadison%20determinantal&limit=30&fields=title,authors,year,url,abstract'),
 ('GitHub','Fuglede Kadison determinantal','https://api.github.com/search/repositories?q=Fuglede+Kadison+determinantal'),
 ('GitHub','determinantal stochastic domination','https://api.github.com/search/repositories?q=determinantal+stochastic+domination'),
]
def fetch(item):
 s,q,u=item; out={'service':s,'query':q,'url':u,'date':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'C0036-mathematical-research/1.0','Accept':'application/json, application/atom+xml'})
  with urllib.request.urlopen(req,timeout=35) as r: data=r.read(); out['http_status']=r.status
  name=s+'_'+str(queries.index(item))+'.raw'; ROOT.joinpath(name).write_bytes(data);out['raw_file']=name
  if s=='OpenAlex':
   obj=json.loads(data);out['results']=[{'id':v['id'],'title':v['title'],'year':v['publication_year'],'doi':v['doi']} for v in obj.get('results',[])]
  elif s=='Crossref':out['results']=[{'title':v.get('title'),'doi':v.get('DOI'),'date':v.get('published')} for v in json.loads(data)['message']['items']]
  elif s=='SemanticScholar':out['results']=json.loads(data)
  elif s=='GitHub':out['results']=json.loads(data).get('items',[])
  else:out['response_preview']=data.decode('utf8')[:18000]
 except Exception as e:out['error']=str(e)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(fetch,queries))
ROOT.joinpath('search_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf8')
for r in results:print(json.dumps(r,ensure_ascii=False)[:22000])
# Fetch direct citations of the correctly identified source.
src=next((r for r in results if r['service']=='OpenAlex' and r['query'].startswith('Determinantal probability')),None)
if src:
 for w in src.get('results',[]):
  if w['title'].lower().replace(',','').startswith('determinantal probability'):
   u='https://api.openalex.org/works?filter=cites:'+w['id'].split('/')[-1]+'&per-page=200'
   try:
    with urllib.request.urlopen(u,timeout=40) as r:data=r.read()
    ROOT.joinpath('openalex_citations.raw').write_bytes(data)
    obj=json.loads(data); rec={'service':'OpenAlex','query':'works citing '+w['id'],'url':u,'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'count':obj['meta']['count'],'results':[{'title':v['title'],'year':v['publication_year'],'doi':v['doi'],'id':v['id']} for v in obj['results']]}
   except Exception as e:rec={'service':'OpenAlex','url':u,'error':str(e)}
   ROOT.joinpath('citation_results.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False),encoding='utf8');print(json.dumps(rec,ensure_ascii=False));break
