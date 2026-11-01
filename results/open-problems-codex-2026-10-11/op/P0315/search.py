import requests, pathlib, concurrent.futures, json, datetime
queries=[('arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"sine beta" AND (all:correlation OR all:Forrester)','start':0,'max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),('openalex','https://api.openalex.org/works',{'search':'sine beta correlation','per-page':50}),('crossref','https://api.crossref.org/works',{'query':'sine beta correlation Forrester Haldane','rows':30}),('semantic','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'sine beta correlation','limit':50,'fields':'title,authors,year,externalIds,url,abstract'}),('github','https://api.github.com/search/repositories',{'q':'"sine beta" correlation','per_page':30}),('openalex_source','https://api.openalex.org/works',{'search':'Long-Range Correlation of Sine beta Point Process','per-page':10}),('arxiv_source','https://export.arxiv.org/api/query',{'id_list':'2603.15289'})]
def fetch(q):
 name,url,params=q
 try:
  r=requests.get(url,params=params,timeout=50); pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8'); outcome=f'HTTP {r.status_code}; saved search_{name}.txt'; print(name,outcome,flush=True)
 except Exception as e: outcome=str(e); print(name,outcome,flush=True)
 return {'date':'2026-10-11','service':name,'url':url,'query':params,'outcome':outcome}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: rows=list(ex.map(fetch,queries))
pathlib.Path('search_log.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
