import requests, pathlib, concurrent.futures, json, datetime
p=pathlib.Path('.')
queries={
'source':'https://arxiv.org/pdf/1611.00411',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:scaling+OR+all:identity)&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search=sandpile%20scaling%20limit&per-page=50',
'crossref':'https://api.crossref.org/works?query=sandpile%20scaling%20limit&rows=40',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query=sandpile%20scaling%20limit&limit=40&fields=title,year,authors,url,abstract',
'github':'https://api.github.com/search/repositories?q=sandpile+scaling+limit&per_page=30'}
def get(k,u):
 try:
  r=requests.get(u,timeout=55,headers={'User-Agent':'MathematicalResearch/1.0'}); (p/(k+('.pdf' if k=='source' else '.json' if k not in ['arxiv'] else '.xml'))).write_bytes(r.content)
  return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-12'}
 except Exception as e: return {'service':k,'url':u,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(lambda kv:get(*kv),queries.items()))
p.joinpath('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('source.pdf');p.joinpath('source.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e: print('PDF extraction:',e)
