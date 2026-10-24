import pathlib,urllib.request,xml.etree.ElementTree as E,json,concurrent.futures
ns={'a':'http://www.w3.org/2005/Atom','r':'http://arxiv.org/schemas/atom'}
for fn,id in [('arxiv_exact.txt','1807.05591'),('sharpness_2_search.txt','0907.2843')]:
 for x in E.parse(fn).findall('a:entry',ns):
  if id in x.findtext('a:id',namespaces=ns):
   print(E.tostring(x,encoding='unicode'))
urls={'sharpness_2':'https://arxiv.org/pdf/0907.2843','sharpness_all_v3':'https://arxiv.org/pdf/1807.05591v3'}
def f(k,u):
 try:
  with urllib.request.urlopen(u,timeout=30) as r: b=r.read()
  pathlib.Path(k+'.pdf').write_bytes(b)
  import pymupdf
  d=pymupdf.open(k+'.pdf');pathlib.Path(k+'_text.txt').write_text('\n'.join(f'=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');return {'service':k,'url':u,'bytes':len(b),'status':200}
 except Exception as e:return {'service':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(lambda kv:f(*kv),urls.items()))
pathlib.Path('search_log_5.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps(r))
