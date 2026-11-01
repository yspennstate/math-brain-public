import urllib.request,urllib.parse,pathlib,concurrent.futures,json
queries=[('resolution_pdf','https://arxiv.org/pdf/2405.20019v2'),('resolution_publisher','https://link.springer.com/article/10.1007/s10959-024-01399-1'),('crossref_resolution','https://api.crossref.org/works/10.1007/s10959-024-01399-1'),('openalex_retry_source','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Slices of Brownian Sheet','per-page':5})),('openalex_resolution','https://api.openalex.org/works/https://doi.org/10.1007/s10959-024-01399-1'),('semantic_resolution','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2405.20019?fields=title,authors,year,externalIds,abstract'),('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0510518?fields=title,externalIds,citations.title,citations.year,citations.externalIds')]
def fetch(x):
 name,url=x
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'D0019-research/1.0'}),timeout=45); b=r.read();pathlib.Path(name+('.pdf' if name.endswith('pdf') else '.response')).write_bytes(b);msg=f'HTTP {r.status}, {len(b)} bytes'
 except Exception as e:msg=f'{type(e).__name__}: {e}';pathlib.Path(name+'.response').write_text(msg,encoding='utf8')
 return name,url,msg
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as p:results=list(p.map(fetch,queries))
with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,msg in results:f.write(f'\n- 2026-10-12 `{name}`: {url}\n  Outcome: {msg}.\n');print(name,msg)
if pathlib.Path('resolution_pdf.pdf').exists():
 import pymupdf
 D=pymupdf.open('resolution_pdf.pdf');pathlib.Path('resolution.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(D)),encoding='utf8')
 for i in range(min(4,len(D))):print('PDF PAGE',i+1,D[i].get_text())
