import urllib.request,urllib.parse,pathlib,concurrent.futures,pymupdf,json
jobs=[('ho','https://arxiv.org/pdf/2007.06100'),('multiplicative','https://arxiv.org/pdf/2009.13848'),('circle','https://arxiv.org/pdf/1903.05327'),('openalex_resolve','https://api.openalex.org/works?filter=doi:https%3A%2F%2Fdoi.org%2F10.30757%2FALEA.v15-15&per-page=1'),('arxiv_modes','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"free Brownian" AND (all:mode OR all:maximum OR all:location)')+'&max_results=50&sortBy=lastUpdatedDate&sortOrder=descending')]
def fetch(job):
 n,u=job
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0177-research'}),timeout=40).read();pathlib.Path(n+('.pdf' if b[:4]==b'%PDF' else '.response')).write_bytes(b)
  if b[:4]==b'%PDF':
   d=pymupdf.open(stream=b,filetype='pdf');pathlib.Path(n+'.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf8')
  return n,u,'OK '+str(len(b))
 except Exception as e:return n,u,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for n,u,r in ex.map(fetch,jobs):
  print(n,r)
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- follow-up '+n+': '+u+'\n  '+r+'\n')
