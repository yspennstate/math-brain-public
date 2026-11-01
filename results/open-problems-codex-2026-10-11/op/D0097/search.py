import requests,json,concurrent.futures,datetime
queries={
'arxiv':'http://export.arxiv.org/api/query?search_query=all:%22activated%20random%20walks%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search=activated%20random%20walks%20critical%20density&per-page=40',
'crossref':'https://api.crossref.org/works?query=activated%20random%20walks%20critical%20density&rows=30',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=activated%20random%20walks%20critical%20density&limit=30&fields=title,authors,year,abstract,externalIds,url',
'github':'https://api.github.com/search/repositories?q=activated+random+walks&per_page=20'}
def run(item):
 k,u=item
 try:
  r=requests.get(u,timeout=70);open(k+'.response','w',encoding='utf8').write(r.text)
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps({'date':'2026-10-12','service':k,'url':u,'http_status':r.status_code})+'\n')
  print(k,r.status_code,r.text[:150],flush=True)
 except Exception as e:print(k,repr(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:list(ex.map(run,queries.items()))
for k in ['openalex','crossref','semantic']:
 try:
  d=json.load(open(k+'.response',encoding='utf8')); items=d.get('results',d.get('data',d.get('message',{}).get('items',[])))
  print('\nSERVICE',k)
  for a in items:print(a.get('publication_year',a.get('year','')),a.get('title'),a.get('doi',a.get('url')),a.get('id',''))
 except Exception as e:print(e)
