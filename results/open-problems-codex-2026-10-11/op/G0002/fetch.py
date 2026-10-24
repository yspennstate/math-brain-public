import urllib.request, pathlib, json, concurrent.futures, datetime
root=pathlib.Path('.')
queries={
 'source_pdf':'https://arxiv.org/pdf/2608.23661',
 'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22second-order%22+AND+all:pivotal&max_results=20',
 'openalex':'https://api.openalex.org/works?search=2608.23661&per-page=10',
 'crossref':'https://api.crossref.org/works?query=second%20order%20pivotal%20Cerf&rows=10',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.23661?fields=title,authors,year,citations.title,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q=%22pivotal%22+%22Cerf%22',
 'arxiv_cerf':'https://export.arxiv.org/api/query?search_query=au:Cerf+AND+submittedDate:[20260801+TO+20261012]&max_results=30'}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  (root/(name+('.pdf' if name=='source_pdf' else '.txt'))).write_bytes(data)
  return {'service':name,'url':url,'date':'2026-10-11','status':status,'bytes':len(data)}
 except Exception as e:return {'service':name,'url':url,'date':'2026-10-11','error':str(e)}
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(fetch,queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results:print(r)
try:
 import pymupdf
 d=pymupdf.open('source_pdf.pdf')
 (root/'source_excerpt.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+d[i].get_text() for i in range(375,min(435,len(d)))),encoding='utf8')
 print('PDF pages',len(d))
except Exception as e:print('extraction',e)
