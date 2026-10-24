import urllib.request,urllib.parse,json,concurrent.futures,pathlib,datetime
P=pathlib.Path(__file__).parent
q='Percolation stable marriage Poisson Lebesgue'
urls={
'source':'https://arxiv.org/pdf/math/0505668',
'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"stable marriage" AND all:percolation')+'&max_results=30',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote(q)+'&per-page=30',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote(q)+'&rows=20',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote(q)+'&limit=20&fields=title,authors,year,externalIds,openAccessPdf',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"stable marriage" percolation')}
def fetch(k,u):
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0085 research bibliography'}),timeout=50); b=r.read();(P/(k+('.pdf' if k=='source' else '.json' if k not in ['arxiv'] else '.xml'))).write_bytes(b)
  return {'service':k,'url':u,'date':'2026-10-11','status':r.status,'bytes':len(b)}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(lambda kv:fetch(*kv),urls.items()))
(P/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results:print(r)
try:
 import pymupdf
 doc=pymupdf.open(P/'source.pdf');(P/'source.txt').write_text('\n'.join('--- PDF PAGE '+str(i+1)+' ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
except Exception as e:print('PDF extraction',e)
