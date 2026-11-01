import urllib.request,pathlib,concurrent.futures,json
urls={'sharpness_all':'https://arxiv.org/pdf/1807.05591','spreadout':'https://arxiv.org/pdf/1912.09825','sharpness_2_search':'https://export.arxiv.org/api/query?search_query=ti:%22Sharpness%20of%20the%20percolation%20transition%20in%20the%20two-dimensional%20contact%20process%22&max_results=5'}
def f(k,u):
 try:
  with urllib.request.urlopen(u,timeout=40) as r:b=r.read()
  fn=k+('.txt' if 'search' in k else '.pdf');pathlib.Path(fn).write_bytes(b)
  if fn.endswith('.pdf'):
   import pymupdf
   d=pymupdf.open(fn);pathlib.Path(k+'_text.txt').write_text('\n'.join(f'=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return {'service':k,'url':u,'bytes':len(b),'status':200}
 except Exception as e:return {'service':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda kv:f(*kv),urls.items()))
pathlib.Path('search_log_4.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps(r))
