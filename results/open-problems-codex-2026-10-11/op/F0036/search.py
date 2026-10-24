import requests, pathlib, json, concurrent.futures, datetime
P=pathlib.Path('.')
queries=[('arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"Brownian net"','max_results':100,'sortBy':'submittedDate','sortOrder':'descending'}),('openalex','https://api.openalex.org/works',{'search':'Brownian net','per-page':100}),('openalex_source','https://api.openalex.org/works',{'search':'The Brownian web the Brownian net and their universality','per-page':5}),('crossref','https://api.crossref.org/works',{'query':'Brownian net most recent common ancestors','rows':40}),('semantic','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1506.00724',{'fields':'title,year,citationCount,citations.title,citations.year,citations.externalIds'}),('github','https://api.github.com/search/repositories',{'q':'"Brownian net"','per_page':30}),('arxiv_exact','http://export.arxiv.org/api/query',{'search_query':'all:"potential most recent common ancestors"','max_results':20})]
def run(q):
 name,url,params=q
 try:
  r=requests.get(url,params=params,timeout=45); (P/(name+'.response')).write_text(r.text,encoding='utf8'); return {'service':name,'url':r.url,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-12'}
 except Exception as e: return {'service':name,'url':url,'query':params,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: out=list(ex.map(run,queries))
P.joinpath('search_log.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for x in out: print(json.dumps(x))
