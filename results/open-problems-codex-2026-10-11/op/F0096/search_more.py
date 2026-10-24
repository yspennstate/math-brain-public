from search import fetch
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
jobs={
'improved':'https://arxiv.org/pdf/1906.01433',
'publications':'https://www.math.cmu.edu/~af1p/papers.html',
'arxiv_recent':'http://export.arxiv.org/api/query?'+urlencode({'search_query':'(all:hamiltonicity OR all:"Hamilton cycles") AND (all:"degree sequence" OR all:"minimum degree three" OR all:"minimum degree 3")','sortBy':'submittedDate','sortOrder':'descending','max_results':60}),
'openalex_retry':'https://api.openalex.org/works?'+urlencode({'search':'Hamilton cycles random graphs minimum degree','per_page':10}),
'openalex_source':'https://api.openalex.org/works?'+urlencode({'search':'Alan Frieze Random structures algorithms ICM','per_page':5}),
'openalex_improved':'https://api.openalex.org/works/https://doi.org/10.1002/rsa.20978',
'semantic_doi':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rsa.20978?fields=title,year,citations.title,citations.year,citations.externalIds',
}
with ThreadPoolExecutor(max_workers=5) as p:
 for o in p.map(lambda kv:fetch(*kv),jobs.items()): print(o,flush=True)
import pymupdf,pathlib
try:
 d=pymupdf.open('improved.txt')
 pathlib.Path('improved_extracted.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
except Exception as e: print(e)
