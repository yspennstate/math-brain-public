import pathlib,requests,json,concurrent.futures
from urllib.parse import quote
jobs={
'openalex_lookup':'https://api.openalex.org/works?filter=locations.landing_page_url:https%3A%2F%2Farxiv.org%2Fabs%2F2608.06358&per-page=5',
'openalex_citations':'https://api.openalex.org/works?filter=cites:arxiv:2608.06358&per-page=50',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query='+quote('sharp threshold tree universality')+'&limit=20&fields=title,year,externalIds,abstract',
'arxiv_recent':'http://export.arxiv.org/api/query?search_query='+quote('(all:"spanning trees" OR all:"bounded-degree trees" OR all:"tree universality") AND submittedDate:[202608060000 TO 202610122359]')+'&max_results=80&sortBy=submittedDate&sortOrder=descending',
'crossref_exact':'https://api.crossref.org/works?query.title='+quote('sharp threshold tree universality')+'&filter=from-pub-date:2026-08-06&rows=20',
'hamilton_source':'https://arxiv.org/pdf/1402.0771'
}
def get(it):
 k,u=it
 try:
  r=requests.get(u,timeout=35); pathlib.Path(k+('.pdf' if k=='hamilton_source' else '.txt')).write_bytes(r.content); return dict(service=k,url=u,status=r.status_code,bytes=len(r.content),date='2026-10-12')
 except Exception as e:return dict(service=k,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:a=list(ex.map(get,jobs.items()))
old=json.loads(pathlib.Path('search_log.json').read_text()); old+=a; pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2));print(json.dumps(a,indent=2))
import pymupdf
p=pathlib.Path('source_text.txt');p.write_text(p.read_text().replace('\x00',''),encoding='utf8')
try:
 d=pymupdf.open('hamilton_source.pdf');pathlib.Path('hamilton_text.txt').write_text('\n'.join(f'--- PAGE {i+1} ---\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
except Exception as e:print(e)
