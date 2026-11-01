import urllib.request,json,pathlib,concurrent.futures
q={'openalex_correct_source':'https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP170','openalex_citing_source':'https://api.openalex.org/works?filter=cites:doi:10.1214/08-AIHP170&per-page=100','factor_pdf':'https://arxiv.org/pdf/2106.04524','unbalanced_pdf':'https://arxiv.org/pdf/2609.19426'}
def f(k,u):
 try:
  with urllib.request.urlopen(u,timeout=40) as r:b=r.read()
  name=k+('.pdf' if k.endswith('_pdf') else '.json');pathlib.Path(name).write_bytes(b)
  if name.endswith('.pdf'):
   import pymupdf
   d=pymupdf.open(name);pathlib.Path(k+'.txt').write_text('\n'.join('\nPDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return dict(service=k,url=u,date='2026-10-11',file=name,bytes=len(b))
 except Exception as e:return dict(service=k,url=u,date='2026-10-11',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:a=list(ex.map(lambda kv:f(*kv),q.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
