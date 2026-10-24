from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json
root=Path('.')
jobs={
'linear2024':'https://arxiv.org/pdf/2406.17891',
'singular2020':'https://arxiv.org/pdf/2009.01299',
'general_regular':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"regularity" AND (all:"switching" OR all:"PDMP")')+'&max_results=40&sortBy=submittedDate&sortOrder=descending',
'torus2017':'https://arxiv.org/pdf/1708.01390',
'crossref_exact':'https://api.crossref.org/works?query.title='+urllib.parse.quote('Some simple but challenging Markov processes')+'&rows=3',
'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('Some simple but challenging Markov processes')+'&per_page=3',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1412.7516?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
'github_retry':'https://api.github.com/search/repositories?q='+urllib.parse.quote('random switching vector fields')}
def job(item):
 k,u=item
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'mathematical-research'}),timeout=45) as f:b=f.read()
  fn=k+('.pdf' if '/pdf/' in u else '.json');(root/fn).write_bytes(b)
  if fn.endswith('.pdf'):
   import pymupdf
   d=pymupdf.open(root/fn);(root/(k+'.txt')).write_text('\n'.join(f'--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return k,u,'OK',len(b)
 except Exception as e:return k,u,str(e),0
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=8).map(job,jobs.items()))
with open('LITERATURE.md','a',encoding='utf8') as f:
 for k,u,s,n in r:f.write(f'\n- 2026-10-12 {k}: `{u}` — {s}; {n} bytes.\n')
print(json.dumps(r,indent=2))
s=Path('source.txt').read_text(encoding='utf8');i=s.index('4\nSwitched');print(s[i:i+4000])
