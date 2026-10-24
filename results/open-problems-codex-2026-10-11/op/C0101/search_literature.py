import requests, json, concurrent.futures, datetime
from pathlib import Path
ROOT=Path(__file__).parent
queries=[
 ('arxiv','integer superharmonic matrices','https://export.arxiv.org/api/query',{'search_query':'all:"integer superharmonic"','max_results':50}),
 ('arxiv','higher dimensional sandpile matrices','http://export.arxiv.org/api/query',{'search_query':'all:sandpile AND all:superharmonic','max_results':50}),
 ('openalex','integer superharmonic matrices','https://api.openalex.org/works',{'search':'integer superharmonic matrices','per-page':100}),
 ('openalex','source lookup','https://api.openalex.org/works',{'search':'Laplacian growth sandpiles and scaling limits','per-page':5}),
 ('crossref','integer superharmonic matrices','https://api.crossref.org/works',{'query':'integer superharmonic matrices','rows':40}),
 ('semantic_scholar','integer superharmonic matrices','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'integer superharmonic matrices','limit':50,'fields':'title,authors,year,externalIds,abstract,url'}),
 ('github','integer superharmonic','https://api.github.com/search/repositories',{'q':'"integer superharmonic"','per_page':50}),
 ('github','sandpile higher dimension','https://api.github.com/search/repositories',{'q':'sandpile higher dimension','per_page':50}),
]
def run(q):
 s,term,url,params=q
 rec={'date':'2026-10-12','service':s,'query':term,'url':url,'params':params}
 try:
  r=requests.get(url,params=params,timeout=50,headers={'User-Agent':'Mathematical-research-C0101/1.0'})
  rec.update(status=r.status_code,request_url=r.url)
  out=ROOT/(s+'_'+str(queries.index(q))+'.txt'); out.write_text(r.text,encoding='utf-8'); rec['response_file']=out.name
  if r.status_code==200:
   if s=='arxiv': print(s,term,r.text[:400])
   else:
    data=r.json(); items=data.get('results', data.get('data',data.get('items',data.get('message',{}).get('items',[]))))
    for x in items:
     title=x.get('title',x.get('display_name',x.get('full_name','')))
     print(s,title,x.get('publication_year',x.get('year','')),x.get('id',x.get('DOI','')))
 except Exception as e: rec['error']=str(e)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(run,queries))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 f.write('\n## API searches, 2026-10-12\n')
 for r in results: f.write('- '+json.dumps(r,ensure_ascii=False)+'\n')
