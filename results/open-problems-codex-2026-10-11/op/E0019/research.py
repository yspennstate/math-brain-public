from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures, datetime
root=Path(__file__).resolve().parent
queries={
'source': 'https://arxiv.org/pdf/1412.7516',
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"invariant density" AND all:"switching"')+'&max_results=20',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('regularity invariant density randomly switched vector fields')+'&per-page=15',
'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('Some simple but challenging Markov processes')+'&per-page=5',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('invariant density randomly switched vector fields')+'&rows=15',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('regularity invariant density switching')+'&limit=10&fields=title,authors,year,url,externalIds',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('PDMP invariant density')}
def run(item):
 k,u=item
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'E0019-mathematical-research/1.0'})
  with urllib.request.urlopen(req,timeout=50) as f: b=f.read()
  (root/(k+('.pdf' if k=='source' else '.json'))).write_bytes(b)
  return k,u,'OK',len(b)
 except Exception as e: return k,u,str(e),0
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(run,queries.items()))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('# Literature search\n\nDate: 2026-10-12. Raw responses saved locally.\n\n')
 for k,u,s,n in results: f.write(f'- {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 d=pymupdf.open(root/'source.pdf'); text='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)); (root/'source.txt').write_text(text,encoding='utf8'); print(text[-18000:])
except Exception as e: print('PDF extraction:',e)
