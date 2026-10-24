import requests, concurrent.futures, json, pathlib, datetime
from urllib.parse import quote
jobs={
'source_pdf':'https://arxiv.org/pdf/2608.06358',
'source_html':'https://arxiv.org/html/2608.06358v1',
'arxiv':'http://export.arxiv.org/api/query?search_query='+quote('all:"tree universality" OR all:"optimal linking systems"')+'&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search='+quote('tree universality random graphs')+'&per-page=30',
'openalex_source':'https://api.openalex.org/works?search='+quote('Universality in random graphs via optimal linking systems')+'&per-page=5',
'crossref':'https://api.crossref.org/works?query='+quote('tree universality random graphs')+'&rows=25',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.06358?fields=title,authors,year,citations.title,citations.externalIds,citations.year',
'github':'https://api.github.com/search/repositories?q='+quote('tree universality random graphs'),
}
def fetch(item):
 k,u=item
 try:
  r=requests.get(u,timeout=50); suffix='.pdf' if k=='source_pdf' else '.txt'; pathlib.Path(k+suffix).write_bytes(r.content)
  return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-12'}
 except Exception as e: return {'service':k,'url':u,'error':str(e),'date':'2026-10-12'}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: results=list(ex.map(fetch,jobs.items()))
pathlib.Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 d=pymupdf.open('source_pdf.pdf'); pathlib.Path('source_text.txt').write_text('\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8'); print('pdf pages',len(d))
except Exception as e: print(e)
