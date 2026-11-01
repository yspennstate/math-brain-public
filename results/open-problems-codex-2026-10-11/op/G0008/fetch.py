import urllib.request, concurrent.futures, json, datetime
from pathlib import Path
urls={
'source_pdf':'https://arxiv.org/pdf/2601.00291',
'source_abs':'https://arxiv.org/abs/2601.00291',
'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+all:%22monotonicity%22&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search=probability%20connection%20monotone%20percolation&per-page=25',
'crossref':'https://api.crossref.org/works?query=percolation%20connection%20monotonicity&rows=25',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2601.00291?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
'github':'https://api.github.com/search/repositories?q=percolation+monotonicity'}
def get(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'G0008-mathematical-research/1.0'}),timeout=45); b=r.read(); Path(k+('.pdf' if k=='source_pdf' else '.response')).write_bytes(b); return k,r.status,len(b)
 except Exception as e:
  Path(k+'.error').write_text(str(e)); return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(lambda kv:get(*kv),urls.items()))
Path('LITERATURE.md').write_text('# Literature search\n\nDate: 2026-10-11 (local). All requests use Python urllib; response files preserved.\n\n'+''.join(f'- {k}: `{u}` — {next(r for r in results if r[0]==k)}\n' for k,u in urls.items()),encoding='utf8')
print(results)
try:
 import pymupdf
 d=pymupdf.open('source_pdf.pdf'); s='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)); Path('source.txt').write_text(s,encoding='utf8'); print(s[:26000])
except Exception as e: print('PDF extraction',e)
