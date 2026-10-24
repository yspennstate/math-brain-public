import requests, json, pathlib, concurrent.futures, datetime
from urllib.parse import urlencode
ROOT=pathlib.Path(__file__).resolve().parent
jobs={
'source': 'https://arxiv.org/pdf/2109.01252',
'arxiv': 'https://export.arxiv.org/api/query?'+urlencode({'search_query':'all:"geodesic" AND (all:"thick points" OR all:"thickness" OR all:"multifractal")','start':0,'max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),
'openalex_search': 'https://api.openalex.org/works?'+urlencode({'search':'Liouville quantum gravity geodesic thick points','per-page':50}),
'openalex_source': 'https://api.openalex.org/works?'+urlencode({'search':'Introduction to the Liouville quantum gravity metric','per-page':5}),
'crossref': 'https://api.crossref.org/works?'+urlencode({'query':'Liouville quantum gravity geodesic thick points','rows':40}),
'semantic': 'https://api.semanticscholar.org/graph/v1/paper/search?'+urlencode({'query':'Liouville quantum gravity geodesic thick points','limit':40,'fields':'title,authors,year,externalIds,url,abstract'}),
'github':'https://api.github.com/search/repositories?'+urlencode({'q':'LQG geodesic thick points','per_page':30})}
def fetch(item):
 key,url=item
 try:
  r=requests.get(url,timeout=65,headers={'User-Agent':'D0051-mathematical-literature-check/1.0'})
  (ROOT/(key+('.pdf' if key=='source' else '.response'))).write_bytes(r.content)
  entry={'service':key,'url':url,'date':str(datetime.date.today()),'status':r.status_code,'bytes':len(r.content)}
 except Exception as e: entry={'service':key,'url':url,'error':str(e),'date':str(datetime.date.today())}
 with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(entry)+'\n')
 return entry
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for r in pool.map(fetch,jobs.items()):print(json.dumps(r),flush=True)
try:
 import pymupdf
 d=pymupdf.open(ROOT/'source.pdf');(ROOT/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
except Exception as e: print('PDF extraction:',e)
