from search import fetch
import concurrent.futures, json, urllib.parse, pathlib
tasks={
'openalex_retry':'https://api.openalex.org/works?search=Nonrigidity%20properties%20Coulomb&per_page=10',
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1214/25-AOP1787',
'arxiv_riesz_recent':'https://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:gas&sortBy=submittedDate&sortOrder=descending&max_results=60',
'arxiv_nonrigidity':'https://export.arxiv.org/api/query?search_query=all:nonrigidity+OR+all:non-rigidity&sortBy=submittedDate&sortOrder=descending&max_results=40',
'optimal_transport_pdf':'https://arxiv.org/pdf/2510.17257',
'stationary_pdf':'https://arxiv.org/pdf/2409.18519',
'circular_pdf':'https://arxiv.org/pdf/2104.09408',
'leblé_pdf':'https://arxiv.org/pdf/2410.04958',
'github_gas':'https://api.github.com/search/repositories?q=Riesz+gas&per_page=30',
'crossref_source':'https://api.crossref.org/works/10.1214/25-AOP1787'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 for r in pool.map(fetch,tasks.items()): print(*r,flush=True)
from pypdf import PdfReader
for name in tasks:
 if name.endswith('pdf') and pathlib.Path(name+'.pdf').exists():
  p=PdfReader(name+'.pdf'); pathlib.Path(name+'_text.txt').write_text('\n'.join(x.extract_text() for x in p.pages),encoding='utf8')
  print(name, '\n'.join(x.extract_text() for x in p.pages[:2]),flush=True)
