import json,pathlib,urllib.request,urllib.parse,concurrent.futures,pymupdf
urls={
'janson':'https://arxiv.org/pdf/0804.1656',
'choi':'https://arxiv.org/pdf/2108.12082',
'new2026':'https://arxiv.org/pdf/2610.04420',
'balogh':'https://math.illinois.edu/~jobal/cikk/bootfig.pdf',
'oa_title':'https://api.openalex.org/works?filter=title.search:'+urllib.parse.quote('Noise sensitivity in bootstrap percolation')+'&per-page=5',
's2_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1509.08454/citations?fields=title,year,externalIds&limit=100',
'arxiv_quenched':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"k-core" AND (all:"quenched" OR all:"noise")')+'&max_results=30'
}
def f(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Probability research'}),timeout=45).read()
  if k in ['janson','choi','new2026','balogh']:
   pathlib.Path(k+'.pdf').write_bytes(b);d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));pathlib.Path(k+'.txt').write_text(s,encoding='utf8');print(k,s[:1700])
  else:pathlib.Path(k+'.data').write_bytes(b);print(k,'OK',b[:120])
  return [k,u,'OK']
 except Exception as e:print(k,e);return [k,u,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:r=list(ex.map(lambda kv:f(*kv),urls.items()))
pathlib.Path('search_log3.json').write_text(json.dumps({'date':'2026-10-12','results':r},indent=2),encoding='utf8')
