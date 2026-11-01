import requests,pathlib,concurrent.futures
qs=[('arxiv_variants','https://export.arxiv.org/api/query',{'search_query':'all:"Sineβ" OR all:"Sine_beta" OR (au:Qu AND au:Valko) OR (all:"pair correlation" AND all:beta)','max_results':100,'sortBy':'submittedDate','sortOrder':'descending'}),('crossref_title','https://api.crossref.org/works',{'query.title':'On the pair correlation function of the Sine beta process','rows':15}),('tail','https://arxiv.org/pdf/2610.10849',{})]
def f(q):
 n,u,p=q
 try:
  r=requests.get(u,params=p,timeout=45);pathlib.Path('search_'+n+('.pdf' if n=='tail' else '.txt')).write_bytes(r.content);print(n,r.status_code,flush=True)
  if n=='tail' and r.status_code==200:
   import pymupdf;d=pymupdf.open('search_tail.pdf');pathlib.Path('tail.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf8')
  out=f'HTTP {r.status_code}'
 except Exception as e:out=str(e)
 return dict(date='2026-10-11',service=n,url=u,query=p,outcome=out)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(f,qs))
import json;p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+rs,indent=2),encoding='utf8')
