import pathlib, urllib.request, json, concurrent.futures
urls={
'arxiv_exact':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:%22percolation%22%20OR%20all:%22invariant%22)&sortBy=submittedDate&sortOrder=descending&max_results=100',
'arxiv_since':'http://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20submittedDate:[20260909%20TO%20261012]&max_results=100',
'openalex_retry':'https://api.openalex.org/works?search=contact%20process%20percolation&per_page=25',
'openalex_source':'https://api.openalex.org/works/https://arxiv.org/abs/2609.09972',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=contact%20process%20percolation&limit=20&fields=title,year,externalIds',
'liggett_pdf':'https://arxiv.org/pdf/math/0504530',
'rath_search':'https://export.arxiv.org/api/query?search_query=ti:%22threshold%20of%20spread-out%20contact%20process%22&max_results=5'
}
def go(k,u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'G0006 Research'}),timeout=40) as r: b=r.read(); st=r.status
  fn=k+('.pdf' if k.endswith('pdf') else '.txt'); pathlib.Path(fn).write_bytes(b)
  out={'service':k,'url':u,'status':st,'bytes':len(b),'file':fn}
  if fn.endswith('.pdf'):
   import pymupdf
   doc=pymupdf.open(fn); pathlib.Path(k+'_text.txt').write_text('\n'.join(f'=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e: out={'service':k,'url':u,'error':str(e)}
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: out=list(ex.map(lambda x:go(*x),urls.items()))
pathlib.Path('search_log_2.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for a in out: print(json.dumps(a))
