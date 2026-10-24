import urllib.request, urllib.parse, concurrent.futures,pathlib,pymupdf,json,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parent
jobs=[('sznitman2012','https://arxiv.org/pdf/1010.1490'),('geometry','https://arxiv.org/pdf/1811.05970'),('signclusters','https://arxiv.org/pdf/1708.03285'),('fpp2023','https://arxiv.org/pdf/2309.03880'),('zeroone2026','https://arxiv.org/pdf/2603.10896'),('arxiv_exact','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"random interlacements" AND (all:graphs OR all:gasket OR all:positivity)')+'&max_results=100&sortBy=submittedDate&sortOrder=descending'),('openalex_citing','https://api.openalex.org/works?filter=cites:doi:10.1007/978-3-319-05852-8&per-page=100'),('semantic_book','https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-319-05852-8?fields=title,year,citations.title,citations.year,citations.externalIds')]
def get(job):
 n,u=job
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research/1.0'}),timeout=50) as r: b=r.read()
  ext='.pdf' if b.startswith(b'%PDF') else '.xml' if n=='arxiv_exact' else '.json'
  (root/(n+ext)).write_bytes(b)
  if ext=='.pdf': (root/(n+'.txt')).write_text('\n'.join(p.get_text() for p in pymupdf.open(stream=b,filetype='pdf')),encoding='utf8')
  res=n+' OK '+str(len(b))
 except Exception as e: res=n+' ERROR '+str(e)
 with (root/'LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- 2026-10-11 | '+n+' | `'+u+'` | '+res+'\n')
 return res
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for r in ex.map(get,jobs): print(r)
