from pathlib import Path
import urllib.request,json,concurrent.futures,pymupdf
qs={'zerner_archive':'https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/ECP/Vol.7/paper19.pdf','zerner_emis_archive':'https://www.emis.de/journals/EJP-ECP/ECP/Vol.7/paper19.pdf','zerner_author_publications':'https://www.math.uni-tuebingen.de/user/zerner/publications.html'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();ext='.html' if 'publications' in k else '.pdf';Path(k+ext).write_bytes(b)
  if ext=='.pdf':
   try:
    doc=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'=== PDF PAGE {i+1} ===\n'+pg.get_text() for i,pg in enumerate(doc));Path(k+'.txt').write_text(s,encoding='utf8');return k,r.status,len(b),s[:14000]
   except Exception as e:return k,r.status,len(b),str(e)
  return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_archive_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':[x[:3] for x in rs]},indent=2))
for r in rs:print(r)
