import urllib.request, urllib.parse, json, pathlib, concurrent.futures
root=pathlib.Path(__file__).parent
q={
'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('2608.21125')+'&per_page=5',
'openalex_citing_identifier':'https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2608.21125&per_page=20',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('threshold cascades unimodular')+'&limit=10&fields=title,year,externalIds',
'arxiv_recent':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"threshold cascades" AND submittedDate:[20260821 TO 20261011]')+'&max_results=50',
'arxiv_chen':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"necessary and sufficient condition" AND au:Chen AND all:"derivative martingale"')+'&max_results=5',
'aidekon_pdf':'https://arxiv.org/pdf/1101.1810',
'companion_pdf':'https://arxiv.org/pdf/2608.15987'}
def f(item):
 name,url=item
 rec={'service':name,'url':url,'date':'2026-10-11'}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MathematicsResearch/1.0'}),timeout=35) as r:data=r.read();rec['status']=r.status
  path=root/(name+('.pdf' if name.endswith('_pdf') else '.txt'));path.write_bytes(data);rec.update(file=path.name,bytes=len(data))
  if name.endswith('_pdf'):
   import pymupdf
   doc=pymupdf.open(path);(root/(name+'_extracted.txt')).write_text('\n'.join(f'=== PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e:rec['error']=str(e)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:r=list(p.map(f,q.items()))
(root/'search_log_round2.json').write_text(json.dumps(r,indent=2),encoding='utf8')
for x in r:print(json.dumps(x))
