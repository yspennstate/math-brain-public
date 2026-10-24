import concurrent.futures, json, datetime, pathlib, requests, subprocess
P=pathlib.Path(__file__).resolve().parent
queries=[
('arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"connective constant" AND (all:expansion OR all:divergence)','max_results':40}),
('openalex','https://api.openalex.org/works',{'search':'connective constant asymptotic expansion divergence','per-page':40}),
('openalex_source','https://api.openalex.org/works',{'search':'Lectures on self-avoiding walks','per-page':5}),
('crossref','https://api.crossref.org/works',{'query':'connective constant asymptotic expansion divergence','rows':30}),
('semantic_scholar','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'connective constant asymptotic expansion','limit':30,'fields':'title,authors,year,abstract,url,externalIds'}),
('github','https://api.github.com/search/repositories',{'q':'self avoiding walk connective constant','per_page':30}),
('openalex_graham','https://api.openalex.org/works',{'search':'Borel type bounds self avoiding walk Graham','per-page':10}),
('openalex_clisby','https://api.openalex.org/works',{'search':'Clisby Liang Slade self avoiding walk','per-page':10}),
]
def fetch(item):
 name,url,params=item
 try:
  r=requests.get(url,params=params,timeout=40,headers={'User-Agent':'C0097 research literature check'})
  (P/(name+'.response')).write_text(r.text,encoding='utf-8')
  out={'service':name,'url':r.url,'status':r.status_code,'date':'2026-10-12'}
  if r.status_code==200 and name!='arxiv':
   data=r.json(); results=data.get('results',data.get('data',data.get('items',data.get('message',{}).get('items',[]))))
   out['works']=[{'title':x.get('title',x.get('full_name')), 'year':x.get('publication_year',x.get('year')), 'id':x.get('id'), 'doi':x.get('doi',x.get('DOI'))} for x in results]
  print(json.dumps(out,ensure_ascii=False),flush=True)
  return out
 except Exception as e:
  out={'service':name,'url':url,'params':params,'error':str(e),'date':'2026-10-12'}; print(out,flush=True); return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 log=list(ex.map(fetch,queries))
(P/'search_log.json').write_text(json.dumps(log,indent=2,ensure_ascii=False),encoding='utf-8')
source=next((x for x in log if x['service']=='openalex_source'),{})
for work in source.get('works',[]):
 if 'Lectures' in str(work['title']):
  result=fetch(('openalex_citing','https://api.openalex.org/works',{'filter':'cites:'+work['id'].split('/')[-1],'per-page':200,'sort':'publication_date:desc'}))
  log.append(result); break
(P/'search_log.json').write_text(json.dumps(log,indent=2,ensure_ascii=False),encoding='utf-8')
paths=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf-8').stdout.splitlines()
hits=[x for x in paths if 'C0097' in x or 'connective' in x.lower()]
(P/'recorded_paths.txt').write_text('\n'.join(hits),encoding='utf-8')
print('Recorded paths:',hits[:30],flush=True)
