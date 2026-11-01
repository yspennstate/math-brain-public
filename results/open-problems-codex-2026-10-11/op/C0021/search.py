import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
P=pathlib.Path(__file__).parent
queries=[
 ('source','https://arxiv.org/pdf/1102.5761'),
 ('arxiv','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"recursive majority" OR all:"iterated majority"','max_results':40})),
 ('openalex','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'recursive majority randomized query complexity','per-page':30})),
 ('openalex_source','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Noise sensitivity of Boolean functions and percolation','per-page':5})),
 ('crossref','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'recursive majority randomized decision tree','rows':20})),
 ('semantic','https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'recursive majority','limit':30,'fields':'title,authors,year,url,abstract'})),
 ('github','https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'recursive majority'}))]
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (P/(name+('.pdf' if name=='source' else '.json' if name!='arxiv' else '.xml'))).write_bytes(data)
  status=f'OK {len(data)} bytes'
 except Exception as e: status=repr(e)
 return {'date':'2026-10-12','service':name,'url':url,'status':status}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  results=list(ex.map(fetch,queries))
 (P/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results,indent=2))
 try:
  import fitz
  doc=fitz.open(P/'source.pdf')
  (P/'source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf8')
  for i,p in enumerate(doc):
   if 'Exercise VIII.5' in p.get_text(): print('PDF PAGE',i+1,p.get_text())
 except Exception as e: print('PDF extraction',repr(e))
