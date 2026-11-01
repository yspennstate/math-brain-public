import urllib.request, urllib.parse, concurrent.futures, json, pathlib, datetime
P=pathlib.Path(__file__).parent
queries={
'source':'https://www.math.cmu.edu/~af1p/ICM.pdf',
'arxiv':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hamilton cycles" AND all:"minimum degree"','max_results':30}),
'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Hamilton cycles random graphs minimum degree three','per-page':30}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Hamilton cycles random graphs minimum degree at least 3','rows':20}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Hamilton cycles random graphs minimum degree three','limit':20,'fields':'title,authors,year,url,externalIds,abstract'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Hamilton minimum degree random graph','per_page':10}),
'frieze_home':'https://www.math.cmu.edu/~af1p/',
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'F0096-mathematical-literature-check/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  name=k+('.pdf' if k=='source' else '.txt')
  (P/name).write_bytes(data)
  out=f'{k}: OK {len(data)} bytes -> {name}'
 except Exception as e: out=f'{k}: ERROR {e}'
 with (P/'LITERATURE.md').open('a',encoding='utf8') as f: f.write(f'\n- 2026-10-12 {k}: `{u}`. {out}\n')
 return out
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
  for out in pool.map(lambda kv:fetch(*kv),queries.items()): print(out,flush=True)
 try:
  import pymupdf
  doc=pymupdf.open(P/'source.pdf')
  (P/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e: print('PDF extraction',repr(e))
