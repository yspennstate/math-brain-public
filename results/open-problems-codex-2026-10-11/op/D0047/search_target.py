import pathlib,urllib.request,urllib.parse,json,concurrent.futures,xml.etree.ElementTree as E
p=pathlib.Path('.')
qs={'arxiv_rumanov':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('au:Rumanov AND (all:bulk OR all:Painlev*)')+'&max_results=50','arxiv_carousel_all':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Brownian carousel"')+'&max_results=80&sortBy=submittedDate&sortOrder=descending','arxiv_sine_pv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"sine-beta" AND all:"Painlev*"')+'&max_results=40','openalex_citing':'https://api.openalex.org/works?filter=cites:W2797918296&per-page=50'}
def f(k,u):
 try:
  b=urllib.request.urlopen(u,timeout=35).read();(p/(k+'.json')).write_bytes(b);return k,'OK',len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
(p/'search_log_3.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':r},indent=2));print(r)
for fn in ['arxiv_rumanov.json','arxiv_carousel_all.json','arxiv_sine_pv.json']:
 if not (p/fn).exists():continue
 ns={'a':'http://www.w3.org/2005/Atom'};root=E.fromstring((p/fn).read_bytes())
 for e in root.findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:published',namespaces=ns));print(e.findtext('a:summary',namespaces=ns))
