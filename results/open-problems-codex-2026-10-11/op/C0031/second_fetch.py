import pathlib,urllib.request,urllib.parse,concurrent.futures,json,pymupdf,xml.etree.ElementTree as E
R=pathlib.Path(__file__).parent
jobs={
'cook':'https://arxiv.org/pdf/1608.07347',
'jain':'https://arxiv.org/pdf/1908.11255',
'taovu':'https://arxiv.org/pdf/0805.3167',
'inhomogeneous_search':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(ti:"invertibility" OR ti:"singular value") AND (all:"perturbation" OR all:"inhomogeneous") AND cat:math.PR','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'})}
def fetch(x):
 name,url=x
 try:
  with urllib.request.urlopen(url,timeout=45) as f:b=f.read()
  ext='.xml' if 'search' in name else '.pdf';p=R/('second_'+name+ext);p.write_bytes(b)
  if ext=='.pdf':
   d=pymupdf.open(p);t='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+q.get_text() for i,q in enumerate(d));(R/('second_'+name+'.txt')).write_text(t,encoding='utf8')
   print('FETCHED',name,len(b),'\n'+t[:18000],flush=True)
  else:
   ns={'a':'http://www.w3.org/2005/Atom'}
   for e in E.fromstring(b).findall('a:entry',ns):
    title=e.find('a:title',ns).text
    if any(w in title.lower() for w in ['inhomogeneous','perturbation','invertibility','heavy']):print('SEARCH',e.find('a:id',ns).text,title,e.find('a:summary',ns).text[:2500],flush=True)
  status='OK'
 except Exception as e:status=str(e);print(name,status,flush=True)
 return {'url':url,'date':'2026-10-11','status':status}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:log=list(ex.map(fetch,jobs.items()))
(R/'second_search_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
