import requests,pathlib,json,concurrent.futures,xml.etree.ElementTree as E
jobs={
'arxiv_target':'https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(au:Pegden+OR+au:Smart+OR+all:pattern+OR+all:identity)&start=0&max_results=100&sortBy=relevance',
'ellipse':'https://arxiv.org/pdf/2007.05792',
'apollonian':'https://arxiv.org/pdf/1208.4839',
'openalex_source':'https://api.openalex.org/works?search=Laplacian%20growth%20sandpiles%20and%20scaling%20limits&per_page=3',
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411?fields=title,citations.title,citations.year,citations.externalIds',
'crossref_target':'https://api.crossref.org/works?query.bibliographic=sandpile%20identity%20Pegden%20Smart&rows=30'}
def f(k,u):
 try:
  r=requests.get(u,timeout=45);pathlib.Path(k+('.pdf' if k in ['ellipse','apollonian'] else '.xml' if k.startswith('arxiv') else '.json')).write_bytes(r.content)
  out={'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-12'}
  if k in ['ellipse','apollonian'] and r.status_code==200:
   import pymupdf
   d=pymupdf.open(stream=r.content,filetype='pdf');pathlib.Path(k+'.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
  return out
 except Exception as e:return {'service':k,'url':u,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: res=list(ex.map(lambda x:f(*x),jobs.items()))
old=json.load(open('search_log.json'));old+=res;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2));print(json.dumps(res,indent=2))
