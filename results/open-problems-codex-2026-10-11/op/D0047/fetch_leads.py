import pathlib,urllib.request,concurrent.futures,json
p=pathlib.Path('.')
qs={'rumanov':'https://arxiv.org/pdf/1306.2117','valko_virag':'https://arxiv.org/pdf/0712.2000','sine_operator':'https://arxiv.org/pdf/1604.04381','dumaz_malvy':'https://arxiv.org/pdf/2603.15289','semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953/citations?fields=title,year,externalIds&limit=100','openalex_exact':'https://api.openalex.org/works?filter=title.search:Operator%20limits%20of%20random%20matrices&per-page=10'}
def f(k,u):
 try:
  b=urllib.request.urlopen(u,timeout=40).read();(p/(k+('.json' if k in ['semantic_citations','openalex_exact'] else '.pdf'))).write_bytes(b)
  if k not in ['semantic_citations','openalex_exact']:
   import pymupdf
   doc=pymupdf.open(p/(k+'.pdf'));(p/(k+'.txt')).write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+pg.get_text() for i,pg in enumerate(doc)),encoding='utf8')
  return k,'OK',len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
(p/'search_log_4.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':r},indent=2));print(r)
