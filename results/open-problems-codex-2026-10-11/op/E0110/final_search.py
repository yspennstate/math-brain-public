import urllib.request,urllib.parse,concurrent.futures,pathlib
urls={
 'openalex_citing':'https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2Fs11134-019-09610-5&per-page=100',
 'openalex_doi_variant':'https://api.openalex.org/works/doi:10.1007/s11134-019-09610-5',
 'arxiv_loggamma':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"log-gamma" OR all:"Morse") AND (all:"Poincare" OR all:"spectral gap")')+'&max_results=20'}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:b=r.read()
  pathlib.Path(k+'.txt').write_bytes(b);s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:
 for k,u,s in p.map(get,urls.items()):
  print(k,s,flush=True)
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: {u}\n  {s}\n')
